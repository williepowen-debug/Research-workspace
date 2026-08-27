# SAM Maintenance Log

Reverse-chronological log of **structural** changes to SAM's docs, folders, and scripts. Each entry: what changed, why, files touched, boot-impact.

Distinct from `thesis/CHANGELOG.md`, which logs **analytical** changes (thesis-version shifts, channel re-weighting, threshold rebumps).

**Archive convention:** archives live next to their active doc (e.g., `thesis/timeline/ARCHIVE.md`). Root `archive/` is preserved as a legacy graveyard for pre-Mar 18 system rebuild — do not add to it.

---

## 2026-08-27 — 3 scripts (2 new, 1 repaired on three axes) · a TSV schema extension backfilled over 1,129 rows · the ledger-nudge disposition

**NEW — `scripts/rate_differential.py`** (boot-wired). Mechanizes the SAM-41 bar: US leg at **Treasury par-curve primary**, JP leg at own MOF. Built because the check had been carried *"still un-run, next session"* for **eight** sessions — **a check deferred eight times is not a check**. First run found the condition had been met **eight days earlier**. Writes `workbook/RATE_DIFFERENTIAL.tsv`. Its tight-margin warning was **corrected the same day** from *"the instrument cannot resolve"* to *"fragile to the alignment choice — a prompt to TEST, not a reason to withhold a grade,"* with the reversal recorded inline so the next session cannot repeat it.

**NEW — `scripts/xccy_basis.py`** (boot-wired). RED's constructive item from CHG-RED-048. **A PROXY, not the basis, and the docstring says so before any number**: forward leg = CME Sep→Dec futures **spread** (fixed 91d — chosen over spot-vs-front specifically to avoid a roll artefact), USD leg = Treasury 3m **bill not OIS**, JPY leg = **BOJ policy rate, an assumption**. Unit anchor wired as a **hard stop** (implied differential must land 0-8%). Writes `workbook/XCCY_BASIS.tsv`. ⚠️ Availability was **checked before building** — a true 3m basis is not computable here; BOND later verified at the FRED API that **no daily JPY rate series exists at all**.

**REPAIRED ×3 — `scripts/mof_flows.py`**, two of the three found by the guard written for the first:
1. **Alert keyed entirely to the 4-week rolling** while the registered threshold is keyed to the **WEEK** ⇒ it printed 🟢 on the 3rd-largest selling week in 21 years. Fix placed **outside** the rolling block and **not** as an `elif` — either would re-inherit the blindness. **n=3 historically; 10.7% of all trips were invisible.**
2. **Only §1 of the MOF CSV was ever parsed** — the **inward** leg (§2, non-residents buying Japanese securities) was one column offset away for the script's entire life, so *"residents sold foreign bonds"* could never be checked against *"did foreigners buy JGBs?"*
3. **`append_tsv` is idempotent by period, so MOF's revisions never landed** — the TSV silently froze first prints (14/1,129 rows differ, all 2026). New `--check-revisions` mode makes the drift visible. ⛔ **Cols 1-7 deliberately NOT auto-corrected: they are the first-print audit trail and past grades must stay reproducible.**

**SCHEMA — `workbook/MOF_FLOWS.tsv` 7 → 12 columns**, inward leg appended **at the end** so positional readers of cols 1-7 are unaffected; backfilled across all **1,129** rows with a hard guard that cols 1-7 came out **byte-identical** (verified 1,129/1,129, row count preserved). Mapping verified by internal consistency (`subtotal == equity + LT`) on every row, with the outward leg as a passing control. Only code reader is `mof_flows.py` itself; all other references are prose.

**LEDGER-NUDGE DISPOSITION (protocol step 1c-bis — "freeze-or-refresh EACH, or say why not").** Nudge fired on 14 ledgers. **Refresh declined for all, with reasons:**
- **GPIF_FLOWS (29 behind) · TRADE_BALANCE (12) · BIS_GLI (8)** — **low-cadence BY CONSTRUCTION**, not rot: GPIF is quarterly with ~5wk lag, TB is monthly with the next release **9/16**, BIS is quarterly with a ~1-quarter lag. Being "behind" in STATUS-writes is their expected state.
- **The remaining 11 were all refreshed TODAY** by the boot sweep or by this session's builds.
- 📌 **INSTRUMENT OBSERVATION worth recording: the nudge counts STATUS-WRITES, not elapsed time — so a day with 7 STATUS commits makes every ledger read "7 behind" even when it was pulled that morning.** The counter is doing exactly what it says; the reading is an artifact of an unusually high-STATUS-write day and should not be read as staleness. Same class as the other three defects above: **a correct counter measured against the wrong denominator.**

## 2026-08-20 (later) — **`bis_gli.py` + `workbook/BIS_GLI.tsv`: the carry-trade scale question becomes an INSTRUMENT rather than a hand-pull**

**WHY.** The BIS figure that killed the v2.0 candidate's §2 was a one-off manual pull. **A load-bearing number that only exists in a session transcript is not reproducible** ([[finding_loadbearing_number_must_be_reproducible]]), and this one now sits under a retired thesis argument that RED, BOND and NEXUS may all cite.

**BUILT `scripts/bis_gli.py`** — BIS SDMX `WS_GLI` (`stats.bis.org/api/v1`, **no auth, QUARTERLY, ~1-quarter lag**). Writes three series to `workbook/BIS_GLI.tsv`: JPY credit to non-bank borrowers outside Japan (total / bank loans / intl debt securities). **Two-clock** (BIS observation period stored separately from `pulled_at`), **idempotent by (period, series_id)**.

🔑 **THE GUARD THAT MATTERS: a UNIT ANCHOR that hard-stops.** BIS reports `UNIT_MULT`, and misreading it puts every figure out by a factor of 10ⁿ — which would have been invisible because the number would still look plausible. The script checks the same table's **JPY credit to the Japanese government against a known ~¥1,280T** and **exits without writing** if it falls outside ¥900-1,800T. *(That check is why the 2026-08-20 number could be trusted at all — it was run by hand first, then wired in.)* Missing series are **skipped, never written as zero**.

**BOOT IMPACT: none — manual-only, and recorded as such in `CLAUDE.md`'s manual-only register.** BIS is quarterly; a daily boot pull would be noise. Run it when the scale question is live.

---

## 2026-08-20 — **SUB-AGENT STATE FILES GET A CAP AND A ROLL-OFF** (Will-directed) · `boj_ois.py` source-impeachment at row/writer/console · 2 new scripts · 3 new archives · manual-only script register

**WHY.** Will asked whether the sub-agents update their files and whether they need a closeout. **The WRITE step always worked** — all three wrote today (+451 lines). **The defect was that the closeout had a WRITE step and NO PRUNE step**, so `PENDING from Run N` blocks and per-run history accumulated forever. **SAM's own surfaces are capped (STATUS 250 lines, MEMORY 100); the sub-agents had no equivalent and nobody had noticed.**

**MEASURED COST (this is why it was worth a session, not a backlog row):** METSUKE spec 20K + state **370K** = **~100K tokens read before any work**; KURA ~85K; KOYOMI ~35K. **A METSUKE spawn spent roughly a third of a context window reading its own history before looking at a single artifact.** ⚠️ **Already realised, not hypothetical:** METSUKE's PENDING held **97 items**, most moot by a ruling issued 13 days earlier, **surviving 14 runs** because nothing ever asked *"what does this ruling close?"*

**BUILT `scripts/subagent_memory_roll.py`** rather than hand-pruning — *a rule without a mechanism is precisely what failed here.* Design rules, deliberate and not to be relaxed: **MOVE never delete** (byte-conservation verified, refuses to write on loss) · **TERMINAL = an EXPLICIT closure marker; unmarked stays LIVE because silence is never closure** · **archives reference-only, NOT boot-read** · **report-only by default — the sub-agent proposes, SAM applies.**

🔴 **THE DRY RUN CAUGHT A BUG IN THE TOOL ITSELF:** *"keep the last N run blocks in FILE order"* proposed archiving **KURA's Run 12 — that day's run** — because KURA writes newest-first while METSUKE writes oldest-first. **Fixed to keep the highest RUN NUMBERS, order-independent.** *Found only because the tool is report-only by default; that is the argument for the default.*

**RETROACTIVE SWEEP RUN IN THE SAME PASS** — installing a rule and leaving existing state is the exact defect ratified against this morning (METSUKE E1). **METSUKE −31% (365K→251K) · KOYOMI −15% · KURA −7%** (recent runs correctly protected). Nothing deleted; re-run is a clean no-op on all three.

**FILES.** New: `scripts/subagent_memory_roll.py`, `scripts/mof_exceedance.py`, `docket/KOYOMI_MEMORY_ARCHIVE.md`, `METSUKE_MEMORY_ARCHIVE.md`, `workbook/KURA_MEMORY_ARCHIVE.md`, `thesis/V20_CANDIDATE_FLOW_SETS_LEVEL.md`, `thesis/V20_CANDIDATE_SELF_ATTACK_SEALED.md`. Rule appended to `docket/KOYOMI.md`, `METSUKE.md`, `workbook/KURA.md`; check wired into `MEMORY.md` closeout.

**ALSO — `boj_ois.py` SOURCE IMPEACHMENT, expressed where the reader actually looks.** WALTER found `BOJ_OIS.tsv` publishing the dead aggregator figure `quality=ok`, pull-stamped ~30 min *before* the packet retiring it: **the do-not-cite lived only in prose, so the dead number was the freshest-stamped, only machine-readable one SAM published.** Now stamped at the **row** (24 re-stamped), the **WRITER** (`IMPEACHED_SOURCES` — a ledger-only edit would have been re-stamped `ok` by the next pull), and the **console**. ⚠️ **Two defects of that fix, both caught: it silently emptied `prior_curve()` and blanked a working delta column** (a guard against a bad LEVEL disabling a good DERIVATIVE), and the good row is `as_of 8/17` while the newest is `8/19`, so **the only citable figure became the OLDEST**. Both fixed. Also: `jgb_auctions.py` **`break`-on-first-auction removed** (KURA's find — the boot captured at most ONE auction per run, the named mechanism behind two ledger gaps).

**MANUAL-ONLY SCRIPT REGISTER added to `CLAUDE.md`.** boot flags every unwired script by design, and **a flag firing every run for a known-good reason trains you to ignore it** — which is what happened to `grade_8_14_branch.py`, flagged every boot for days while SAM read past it. Three scripts recorded as deliberately manual-only; **anything not on that list is real drift.**

**BOOT IMPACT:** sub-agent spawns read ~37K fewer tokens of their own history. No change to SAM's own boot sequence.

---

## 2026-08-04 (PM, 3rd block) — boot-output defect sweep: `cpi_japan.py` PAIRED/LEAD split · `trade_balance_japan.py` ×2 frozen literals · `catalyst_countdown.py` 2027 guard · PyYAML/DM-v1 unblocked

**Why:** Will asked for a boot, then twice asked to re-check the result. Each re-check found something the previous pass missed — recorded because the *sequence* is the lesson, not any single fix.

**1. `cpi_japan.py` — cross-month comparison labelled as a gap.** `print_comparison_note` differenced the two *latest* value-dicts whatever months they were and called it "Tokyo vs National core-core gap." **Root cause was structural, not arithmetic:** `print_summary_for` returned only `vals` and **discarded the reference month**, so the same-month check its own docstring promised was impossible to perform. On 8/4 it printed **+0.3pp** (Tokyo Jul 2.0 vs National Jun 1.7) against the canonical paired **+0.2pp** (Tokyo Jun 1.9 vs National Jun 1.7) — two figures, one name, hours after SAM corrected that very KB-169 series. Now takes the full by-month maps and prints two **labelled** lines: **PAIRED** (latest month in BOTH series — the only real gap) and **LEAD** (Tokyo ahead of National — "NOT a gap: do not difference across months"). Falls back to an older common month rather than fabricating a cross-month diff. **7 branches tested incl. every negative.** Live API path (6-mo lookback) verified, not just `--summary`.

**2. `trade_balance_japan.py` — TWO frozen date literals, the second found only on re-check.** (a) The "Next release" line printed a hardcoded *"May provisional Wed Jun 17"* unconditionally, so in August it advertised a past date for a release already in the TSV, at rc=0 (`finding_stale_executable_exits_clean`). (b) **Missed on the first pass:** the branch-(c) routing verdict read *"defer to June TB (provisional Jul 22)"* — pointing the reader six weeks into the past. Both now call **`next_scheduled_release()`**, resolved at run time from `docket/CATALYSTS.tsv` (the maintained feed `catalyst_countdown.py` already reads), so they cannot rot independently of the docket. **5 branches tested**; every failure path says "no future Japan-TB row in docket" rather than inventing a date. ⚠️ **Lesson: the first pass fixed the printed LINE, not the CLASS** — the second instance sat ~200 lines away in the same file.

**3. `catalyst_countdown.py` — a silent failure scheduled for 2027-01-01.** `HOLIDAYS` covers **2026 only**, under a comment saying "Extend each calendar year" — a remembered ritual with no mechanism (`finding_mechanize_the_cap_not_the_ritual`). The failure direction is the dangerous one: with no holidays to exclude, the trading-day count goes **UP**, so every catalyst reads **further away / less urgent**, inverting the fail-safe the file's own comment documents. Added **`HOLIDAY_COVERAGE_MAX_YEAR`, derived from the set** so it cannot disagree with it, plus `holiday_coverage_warning()` wired into `main()`. **Deliberately does NOT extend the calendar** — 2027 dates incl. substitute days must be sourced, not guessed; the guard makes the gap announce itself. Both branches tested (silent in coverage, loud past it).

**4. PyYAML installed → DM v1 validator unblocked.** `MESSAGING/tools/validate.py` could not run (PyYAML absent from **both** system python3 and the repo `.venv`), so the ratified DM v1 lane was dead on a live coded route. `pip install -r MESSAGING/requirements.txt` → 6.0.3; verified **rc=0** on real traffic. ⚠️ **`.venv/` is gitignored and machine-local — this does NOT travel.** 🔧 **CORRECTED: the box still missing PyYAML is the one that is NOT `WilliePOwen`.** SAM wrote "the laptop is still broken" repeatedly on 8/4 — **backwards**: `PROME/MACHINE_LOCAL.md` line 7 maps hostname `WilliePOwen` → **LAPTOP**, and that is the box where the install ran. **State this by HOSTNAME, never by nickname** — the hostname→machine label is itself recorded as "believed LAPTOP — Will to confirm." Registered in no provisioning surface: absent from `MACHINE_LOCAL.md`'s rebuild recipe and from `env_doctor`'s `REQUIRED_VENV_DEPS`, while `scripts/requirements.txt` *does* pin `pyyaml==6.0.3` but is **CI-scoped** (installs into a GH Actions runner, never `.venv`) — a pin in the wrong-scope file reads as coverage and is worse than no pin. **`env_doctor` printed `CLEAN` on this box minutes after the outage.** Routed to PROME — ⚠️ **written to the DEAD `AGENTS/PROME/inbox/` path (regrow #5) and migrated by PROME; it now lives at `PROME/inbox/processed/2026-08-04_from-SAM_dm-v1-dependency-in-no-inventory...`.** PROME dispositioned it same day: recipe fixed in `MACHINE_LOCAL.md`, and the `env_doctor` REQUIRED scoping call **re-routed to DAEDALUS** (owns repo-root `scripts/` since 7/31). Auto-memory `finding_verification_zero_is_ambiguous` extended with the third form.

**Boot impact:** none breaking — 12/12 green after each round. Output text changed for CPI (2 labelled lines), TB (derived next-release + branch-(c)), catalyst countdown (conditional warning, silent until 2027).

**Verified NOT defects, left alone:** `cftc_jpy.py` "Jul 2024 peak" and TB `[Apr 2026 anchor: −67.2%]` are labelled historical anchors; `gpif_flows.py` "~Jul 1-3" is a recurring cadence; TB's `2026-01`/`2026-04` ISO dates are selftest fixtures. **Still open (provenance only):** TB ~line 394 cites "CALENDAR Jun-17 row", long since pruned.

---

## 2026-08-04 — `boj_ois.py` BUILT (Will-approved) · **generated TOOL INVENTORY in boot** · `fxy_options.py` plausibility gate · MOF weekly cadence adjudicated · `usdjpy.py --revise-window`

**Why (all four trace to one session's failures, not a tidy-up):**

**1. `scripts/boj_ois.py` — NEW, boot-wired.** SAM sourced BOJ hike pricing by ad-hoc web search. On 8/4 that failed twice in one session: two of three searches returned **2025-vintage** BOJ content reading as current (incl. a "42% October" conflicting with SAM's verified ~64%), and after failing to source it SAM **asserted a direction anyway** and had the **sign backwards** (route 1 is hawkish-*of-priced* — it pays on SURPRISE, so a RISE in priced probability SHRINKS the edge).
- Source: `centralbank.watch/bank-of-japan/`, **server-rendered HTML** (no JS, no JSON API — probed, 404), instrument **3m-TONA futures**.
- **Asserts the CUMULATIVE basis on the page every run and HARD-STOPS without it** — an unverified basis is precisely what produced the sign error. Stored deltas are meaningless if the basis moves silently.
- **Derives what the thesis needs**, not just what the page shows: per-meeting **marginal** = cum(k) − cum(k−1), and **unpriced surprise room** = 100 − cum(k). First run reproduced the hand-computed **60.3% Sep unpriced**.
- **Two-clock (PAT-044):** source's own `as_of_date` stored separately from `pulled_at`; if as-of has not advanced it writes **nothing** (no fabricated fresh rows — `finding_partitioned_source_returns_stale_window_at_200`). Idempotent by (as_of_date, meeting_date).
- **Sanity gates** (the FXY lesson — *computable ≠ trustworthy*): probs in [0,100], cut+hold+hike ≈ 100, cumulative must be **non-decreasing by construction**, meeting dates not before as-of, runaway-parse cap. Failures grade `suspect`, never silently pass.
- **Alert bar is NOT invented here** — it reuses the existing **>5pp named-driver** bar from THESIS § CARRY-UNWIND PROBABILITY METHOD (per the standing rule that script thresholds must match THESIS definitions).
- **15 guard branches unit-tested including every negative case** (basis removed, basis partial, as-of absent, cumulative decreasing, sum≠100, out-of-range, empty parse, meeting-predates-as-of).
- Boot: added to `BOOT_SEQUENCE` after JGB Auctions (~6s); `boot.py` `key_markers` extended so the vintage, the in-window row, the surprise-room line and the single-source caveat surface — same pattern already used for the FXY vol read.
- New file: `workbook/BOJ_OIS.tsv`.

**2. `scripts/fxy_options.py` — plausibility gate.** `_vol_quality` conflated **computable** with **trustworthy**: any RR it could calculate graded `ok`. Added `RR_IMPLAUSIBLE_ABS = 10` vols (deliberately loose — ~2× the widest defensible ETF skew, so it removes garbage not signal). Non-physical readings now grade `rr_implausible`, are excluded from `CALIB_OK_QUALITY`, and print **"UNREADABLE … NO directional read"** instead of a confident "calls bid". **Impact: 30 of 114 historical RR readings (26%) were non-physical and graded `ok` — worst −141.50 — and had been feeding the trailing self-calibration.** `Vol_Quality` re-graded **downgrade-only** (the ok/approx split depends on a note that is not stored and cannot be faithfully recomputed).

**3. `docket/RELEASES.md` — MOF weekly cadence corrected Sat–Fri → Sun–Sat.** Adjudicated against the **primary**, not by preference: MOF's own period strings in `workbook/MOF_FLOWS.tsv` are **6-of-6 Sunday→Saturday**. RELEASES.md's rule was the error; STATUS/CALENDAR were right. ⇒ the Aug-6 "wk 7/26-8/1" label is correct and the 3rd-week BND-11 confirm reads as written — cleared **before** the print.

**4. `scripts/usdjpy.py` — `--revise-window N` backfill hatch.** L3 audited the full 60d hourly lookback but L2 only rewrote inside 10d, so pre-fix truncated rows were re-reported every run and could **never self-heal** — a standing alarm decaying into background noise. Widening rewrites history, so it is a **flag, not a default**. One-off `--revise-window 90` repaired 59 sessions (all under-stating); 1366 rows in/out, second run revises 0, alarm clears.

**5. `scripts/boot.py` — GENERATED TOOL INVENTORY (Will-directed).** A future SAM boot had no way to see what tooling *exists* short of reading source or trusting a hand-written list — and a hand-written list rots **silently**: an unwired script never runs, never prints, and a later session rebuilds it or does its job by hand. Added `tool_inventory()` / `print_tool_inventory()`, derived from `scripts/*.py` at run time and cross-checked against `BOOT_SEQUENCE`:
- **`boot.py --tools`** — full table (name · boot-wired? · one-line purpose parsed from the module docstring), no network, no writes. **Exits 1 on drift** so it can gate a check.
- **Every normal boot** prints `Tools: N in scripts/ (M boot-wired) — full list: boot.py --tools`, and flags drift **in both directions**: on-disk-but-unwired (boot never runs it → invisible to future sessions) and wired-but-absent (boot references a ghost). **Silent when clean**, so it adds no noise.
- Verified on all three branches (orphan / missing / clean) plus exit codes 0 and 1.
- **Deliberately NOT mirrored as a list in `CLAUDE.md`** — CLAUDE.md points at the command instead. Duplicating it would reintroduce exactly the rot this removes. *(Class: mechanize the check, don't ritualize it.)*

**Boot impact:** +1 script (~6s) and a generated inventory line. **Docs:** `CLAUDE.md` (boot step 7 sweep list, manual-fallback source entry with the cumulative-basis + 2025-vintage warnings, FILES table, auto-pulled TSV list), `MEMORY.md` infra queue item 5 closed.

---

## 2026-08-02 — `usdjpy.py` timezone bug fixed (silent false-negative in the disorder detector) · STATUS compressed 409 → 179 · BOJ pre-registration archived

**Trigger:** SAM real boot 8/2 (Will-directed). Boot output showed the threshold monitor and the USDJPY history module disagreeing on the level (157.22 vs 160.71) — chased to a data-integrity bug, then the owed compression pass ran.

1. **`scripts/usdjpy.py` — `merge_and_write()` skip-guard fixed (BUG, high severity).** `today_str` came from `datetime.now()` (local/Eastern) but yfinance labels `USDJPY=X` bars in **Europe/London**. Any boot run after ~19:00 ET therefore saw the next London-day's few-hours-old **partial** bar as "not today" and appended it as final; the idempotent-by-date append then made it permanent, so it never self-corrected. **10 of the last 60 sessions were truncated, every one under-stating the daily range.** Worst: **2026-07-30 stored as a 0.33y range; true range 5.74y** — the intraday-range alert (SAM's independent MOF-disorder detector, CRIT 4.0y) reported *"normal daily range"* on the largest yen move since Dec-2023 and the suspected ~¥8.45T op. Fix: derive "today" in `df.index.tz`; skip `date >= today`. **Boot impact: the detector now fires `INTERVENTION-GRADE 5.74y on 2026-07-30`** — SAM corroborates the op from its own instrument rather than only from the wires. `workbook/USDJPY.tsv` repaired from fresh bars (10 rows) and re-sorted (7/29-7/30 were out of order). Commit `34069b8c0`.
   - **Class note:** a freshness/vintage guard keyed to the *wrong clock*, failing FALSE-NEGATIVE and silently — the same failure shape as [[finding_mtime_is_corrupted_by_git_sync]]. Any future guard comparing a vendor-supplied timestamp against a locally-derived "now" must resolve both in the **same** timezone.
   - **Known remaining defect (flagged, not fixed):** Yahoo's daily FX **Close** field is a bar-boundary snapshot (Open≈Close on every row), so `usdjpy.py`'s headline level is unreliable — it printed 160.18 against a true Friday close of 157.40. Fixing it means changing the level's data source (live quote or hourly bars); deferred as a design decision, not a one-liner.

2. **`STATUS.md` compressed 409 → 179 lines** (250-line cap; 3 sessions overdue, now cleared). Method per [[finding_boot_slimming_dormant_or_settled]] discipline — cut only DORMANT/SETTLED content, not merely duplicated: the mega-banner rewritten to current-state-only (it was still carrying "KEY LIVE (Mon Jul 6)" marks); 7/9, 7/10 AM+PM, 7/11, 7/17, 7/21, 7/23 session notes → one-line pointers (all TIMELINE-mirrored); superseded Jun-3/Jun-14 carry tables → git history; resolved Hard-Trigger and Sep-$60-call blocks → TRADE/CHANGELOG pointers. **Also corrected, not just compressed:** KEY THRESHOLDS, MARKET DATA, INTERVENTION STATUS and WHAT TO WATCH were all still carrying 7/23 values (USD/JPY 163.83, CFTC 68.1%, Brent $100.43) — six weeks of drift behind the banner, the [[finding_status_spine_staleness_under_appended_top]] shape.

3. **`thesis/BOJ_2026-07-31_PREREGISTRATION.md` — NEW.** The resolved July-MPM frozen pre-registration + grade (STATUS lines 18-93) extracted **verbatim via `sed`, not retyped**, with a provenance header. Kept as a retrievable *path* rather than git history alone because the block contains a **contamination clause** that was later invoked and paid off (circulating pre-dated content claimed "GDP upgraded to 0.8%"; actual FY2026 print 0.6) — that makes the freeze an audit artifact. Reference-only; not boot-loaded.

---

## 2026-07-02 — Sub-agent performance review → brief amendments (METSUKE verify-pass mode; KURA full-mode default; rubber-stamp guard)

**Trigger:** Will-directed performance analysis of the trio after the 7/2 parallel run (METSUKE Run-10 / KOYOMI Run-11 / KURA Run-9); recommendations applied same session.

**Review findings (basis for the changes):** METSUKE ~97% cumulative apply rate over 10 runs, zero money-field violations; KOYOMI's best mechanisms are self-built from its own misses (Run-4 auction miss → the baseline audit that today caught the Sep-18 window-end coincidence + the 2025-base CPI discontinuity), clean across 4 model tiers; KURA ~85% promote rate over 9 runs, 1 caught factual error (KB-187), archive-moves never misfired. Trio value concentrates in **mechanical diligence SAM wouldn't schedule** (sibling-instance hunting, calendar-coincidence detection, deadline enforcement), not analysis. Weaknesses: recent 100% accept rates are ambiguous (calibration vs rubber-stamping); per-run cost 10-40× the "typical subagent" line; KOYOMI fetch-layer garble risk (self-flagged "Aug 8" instance).

1. **`METSUKE.md` — RUN MODES section added (new):** `full-sweep` (default) + **`verify-pass`** (codifies Run-10's ad-hoc mode — SAM inline-fixes what it knows it changed, METSUKE hunts residuals only, specifically the two Run-10 failure modes: sibling-instance miss + bracket-with-rotten-interior). Stale "Last run: (none — inaugural)" header line fixed → pointer to MEMORY as canonical.
2. **`workbook/KURA.md` — default mode flipped `propose-only` → `full`** (3 spots: canonical invocation, default sentence, RUN MODES section). Scope unchanged: the flip affects only the single autonomous act (archive-moves of already-SUPERSEDED rows); new-fact adds remain propose-only in both modes. `propose-only` retained for low-trust contexts (post-incident / post-spec-change / SAM mid-edit on workbook).
3. **Rubber-stamp guard installed in all 3 SAM-owned CALIBRATION sections** (METSUKE_MEMORY / KURA_MEMORY / KOYOMI_MEMORY): track declines-per-10-runs; 10 consecutive zero-decline runs force an explicit adversarial read of ≥2 accepted items on the next apply pass. Current tallies seeded (KURA healthiest at 4 declines/re-routes in 9 runs).
4. **MEMORY Feedback trio line updated:** 6/4 consistency-over-yield finding re-validated at the high-watermark extreme + spawn guidance added (cheaper tiers fine for routine KOYOMI/KURA syncs — evidenced by KOYOMI Runs 8-11 across Opus/Sonnet/Fable; big model reserved for post-pivot METSUKE + audit-heavy runs).

**Boot-impact:** none (none of these are boot reads). Next-spawn impact: KURA spawns default `full`; METSUKE spawns name a mode.

---

## 2026-06-22 — RED-dialogue scaffold + doc-ownership cleanup (STATUS→TIMELINE) + steward runs

**Trigger:** Will-directed housekeeping while RED catches up (8-day dark) ahead of the v1.6 convergence (gated on the Mon 3:30 PM ET CFTC Jun-16 EV-print + RED pass).

1. **NEW: `V16_RED_DIALOGUE.md`** — turn-based adversarial surface for the SAM⇄RED v1.6-backbone resolution (baton header + append-only discipline + the 6 pre-registered RED challenges with per-challenge SURVIVES bars + a resolution ledger). Top-level in SAM's dir (SAM-owned/committed; RED appends — a Will-authorized exception to the don't-edit-each-other's-files rule). Temporary task artifact — archives on v1.6 finalize. Boot-impact: none (not a boot read).
2. **STATUS doc-ownership cleanup:** the Jun 1-6 "STATE OF PLAY" play-by-play (resolved narrative) → replaced with a pointer to TIMELINE (RESOLVED blocks Jun 1 / Jun 5-6 / Jun 8-9). **STATUS 326→294 lines.** Cabling evidence retained in § BOJ ASSESSMENT; the OS.1-closure trace preserved. The banner + BOJ-ASSESSMENT-table + WHAT-TO-WATCH compression stays the v1.6 job (still >250 cap).
3. **TIMELINE backfill:** narrated the 5 post-Jun-16 resolved events (FOMC Jun-17 / Iran deal Jun-17 / May-TB Jun-17 / National CPI Jun-19 / Hormuz re-closure Jun-20) as one newest-first block — facts + current framing, conviction re-underwrite deferred to v1.6. **TIMELINE 329→360 lines.** Fixes the stale prune-trail KOYOMI flagged (TIMELINE had been current only through Jun-16).
4. **Steward runs:** KOYOMI Run-9 (docket prune + framing refresh; retained the CFTC peak-fuel row per directive) + KURA Run-7 (full mode; archived KB-SAM-006; watermark 06-19→06-22; surfaced that its `Last harvest:` header had drifted at Run-3/06-03). Both verified clean against ground truth; neither committed.

**Boot-impact:** STATUS shorter (294 lines, still >250 cap pending v1.6); TIMELINE current through Jun-20; +1 temporary dialogue file (not a boot read).

**Deferred:** the 2 minor KOYOMI docket escalations (#2 prune GEOPOLITICAL WATCH >7d resolved rows; #3 relocate the Sato row) → KOYOMI's next run. NEXUS_BRIEF refresh + the MEMORY session-notes rewrite → post-v1.6 closeout.

---

## 2026-06-21 — WIRED NEXUS_BRIEF.md into the SPAWN PROTOCOL (closeout write-back + FILES + Doc-Ownership)

**Trigger:** Will-directed boot-process cleanup. A 7-peer compare/contrast (BRENT/VIOLET/HENRY/CARL/HAWK/LIQUID/REGINALD, via background workflow) found SAM leads the fleet on internal apparatus (10-script boot.py actually wired + clean; calibration scoreboard preamble + PREDICTIONS_ARCHIVE; 3 stewards KOYOMI/METSUKE/KURA; evals/ + RECONCILIATION) but trails on the newer cross-agent plumbing. Specifically `NEXUS_BRIEF.md` — present since the ~Jun-6 NEXUS-schema rollout — was never wired into CLAUDE.md, so it rotted ~2wk stale (body As-of Jun-7, pre-BOJ). The brief's own footer flagged the gap verbatim: "write-back step pending CLAUDE.md amendment."

1. **CLAUDE.md write-back § — new step 13a:** mandatory NEXUS_BRIEF refresh every session, fleet-standard no-change floor (bump As-of + STATUS commit hash). Mirrors BRENT/VIOLET/CARL closeout step 12.
2. **CLAUDE.md MAIL/messaging note:** added NEXUS_BRIEF as the steady-state cross-agent synthesis surface (NEXUS + peers read it in place of raw STATUS).
3. **CLAUDE.md Doc-Ownership table:** added NEXUS_BRIEF row (owns cross-agent synthesis; does NOT duplicate STATUS market tables / TIMELINE narratives).
4. **CLAUDE.md FILES table:** added NEXUS_BRIEF.md row.
5. **NEXUS_BRIEF.md:** footer updated (amendment landed, no longer "pending"); added ⚠️ BODY-STALE banner under As-of (body is pre-BOJ; first full content refresh due at v1.6 finalize).

**Boot-impact:** none at boot (NEXUS_BRIEF is a closeout/write-back surface, not a boot read). +1 mandatory closeout step.

**NOT YET DONE (tracked in MEMORY NEXT SESSION):** the first content refresh of the stale Jun-7 body — deferred to **v1.6 finalize** (analytical marks frozen pending Mon-Jun-22 CFTC + RED). The wiring is in place; the content catch-up rides the v1.6 SIG-to-LIQUID/HENRY pass.

**Out of scope (flagged to Will, PROME-level):** SAM still lacks the WALTER `board_log.tsv` intake lane the rest of the fleet has — deliberately deferred per `[[project_messaging_overhaul]]`, not a SAM-local cleanup.

---

## 2026-06-10 (PM) — NEW SCRIPT: trade_balance_japan.py + TRADE_BALANCE.tsv + boot.py wiring + TB docket date correction

**Trigger:** Will-directed build (infra queue #1), planned with Orch spec review (4 decisions + 4 spec gaps + 3 SAM refinements — all adopted). Purpose: Jun-17 May TB print = Phase-1 stability lag-test; routing pre-registered in CALENDAR.

1. **`scripts/trade_balance_japan.py`** — MOF Customs trade-stats parser. Sources: `d41ma.csv` (headline raw series, CP932, 1979→) + press-release XML `trade-st/{YYYY}/{YYYY}{MM}{stage}.xml` (stage 4=速報/5=確速/6=確報/7=確々報, all stay online). Extracts headline + world crude/LNG/pet-products decomposition (volume 千KL, value, MOF's own YoY) + ME totals + ME crude. Implied crude unit cost ¥/KL→$/bbl (6.29, monthly-avg USDJPY) sanity-banded vs Brent t−1..t−2 avg ±20% (cargo-pricing lag). Routing suggestion uses verbatim CALENDAR branch labels, ME-recovery proxy (≥−20% YoY) printed as stated assumption — measurement not adjudication. Modes: default/`--boot` (fast-exit probe), `--month/--stage`, `--backfill N`, `--selftest`, `--consensus` (hand-fed ¥B).
2. **`workbook/TRADE_BALANCE.tsv`** — NEW auto-pulled TSV, keyed **(Month, Stage)** — provisional + confirmed are separate rows; later stage triggers a "REVISED FROM" comparison print. Backfilled 14 months (Apr 2025–Apr 2026, best stage each). Data note: crude vol 10–14k 千KL/mo through Mar-2026 → **4,480 in April** (supply-destruction cliff is an April event, not a drift); implied unit cost $66–75/bbl 2025 → $101/bbl April (war-tape cargo lag).
3. **`scripts/boot.py`** — wired into BOOT_SEQUENCE after MOF Weekly Flows, `--boot` quiet mode (~4s; one ⚪ line on non-print days). Verified end-to-end, all scripts green.
4. **Docket date correction (CATALYSTS.tsv + CALENDAR.md):** May TB provisional = **Wed Jun 17 08:50 JST (~7:50 PM ET Tue Jun 16 — BOJ-decision evening ET)**, NOT "Jun 18" as docketed; June TB provisional = Jul 22 (not "~Jul 16-17"). Pinned from MOF Customs release calendar (`/toukei/calendar/calend_e.htm`) per Orch spec-gap (c) — the pattern-match date was wrong by a day in the load-bearing direction (earlier). [[finding_subagent_prefire_date_verification]] instance.

**Fixtures (--selftest, frozen):** Apr-2026 stage-4 balance ¥301,905M EXACT (press ¥+301.9B; CSV stage-5 shows +299.3B — stage revision, both in ±1%/±¥5B tolerance), crude vol YoY −63.7 (press "−64%"), ME crude −67.2 exact, exports +14.8 (THESIS cite); Jan-2026 XML-vs-CSV cross-source Δ0.00%. Parser bug caught by fixture on first run: full-width vs half-width parens in body `<title>` elements — normalized.

**Boot-impact:** +1 BOOT_SEQUENCE entry (~4-6s). Next live use: Jun 17 08:50 JST print (run with `--consensus <wire>` that evening ET).

---

## 2026-06-10 (AM) — Script fixes: usdjpy.py MOF label disambiguation + jgb_auctions.py JST date probing

**Trigger:** Both queued from the Jun-9 session's mis-parse incidents; executed in the pre-blackout quiet window (Advisor-endorsed, Will-approved batch).

1. **`scripts/usdjpy.py`** — MOF_INTERVENTIONS labels reformatted `May26` → `May2026` (all 7 entries, MonYYYY). The compact `May26` form read as a day-of-month and propagated a real mis-parse Jun 9 ("MOF May26" → "May 26 intervention"; actual = the **May 6** 2026 op). Comment added pointing at the failure.
2. **`scripts/jgb_auctions.py`** — default and `--catalog` modes now probe from **JST date** (`jst_today()`, UTC+9) instead of local ET date. MOF publishes results under JST dates; the ET-date probe missed the live Jun-10 JST 30Y result on Jun-9 evening ET (fetched by hand that night). Verified post-fix: finds eresul20260610, idempotent on the hand-added TSV row.

**Boot-impact:** none structural — same outputs, correct labels/dates. Both scripts re-run clean.

**Trigger:** NEXUS post-E (E-phase shipped Sat 6/6 PM); SAM proposal/2026-06-06_nexus_brief_schema.md was waiting on ratification. Will signaled rollout for fleet; NEXUS reviewed and proposed 6 amendments + 1 scope clarification. Will accepted all amendments, rejected the SENDING-table drop-rule (kept single-table-per-Will convention), and tasked SAM with drafting both the canonical SAM brief and a fleet template.

**Amendments applied (NEXUS R3):**
1. `Recent thesis pivot:` required single line (named what + why) — captures the leading-edge-of-convergence signal NEXUS wanted at boot.
2. `Cross-agent tensions known to me:` required (was optional) — "None active this cycle" forced bullet prevents silent decay of the asymmetric-info channel.
3. `WATCH` renamed `FORWARD CATALYSTS`; `NEXT DECISION POINT` carved out as the agent-actioned subset that triggers a brief refresh — disambiguates monitoring-list from action-trigger.
4. Status emoji semantics locked to CLAUDE.md key (🟢 none / 🟡 monitoring / 🟠 elevated / 🔴 active/critical) — fleet-wide comparability.
5. Conviction decomposition made optional per agent (direction/timing/level where domain has clean math; single-letter conviction otherwise) — avoids fake decomposition for HAWK/BROCK-style domains.
6. Scope clarified: Tier-1 agents only (CARL, REGINALD, OZK, SAM, RED, BROCK, LIQUID, HENRY, HAWK, BRENT, VIOLET, WALTER + NEXUS itself). Tier-2 spawn-as-needed agents skip the brief; NEXUS reads their STATUS directly when active.
7. Single SENDING table (per Will, against NEXUS's drop-row suggestion) — refresh discipline at session closeout per SPAWN PROTOCOL; agent owns the freshness.

**Files touched:**
- `AGENTS/SAM/NEXUS_BRIEF.md` — pilot brief promoted to canonical schema path; 75 lines; Type B convergence candidate flagged (catalyst-path decoupling — Jun 5 USDJPY 160 via USD-side NFP rather than MOU/oil path).
- `AGENTS/SAM/proposals/2026-06-07_nexus_brief_template.md` — fleet template draft with inline rubric comments; pending promotion to `AGENTS/NEXUS/templates/NEXUS_BRIEF_TEMPLATE.md` (SAM doesn't write outside its dir).
- `AGENTS/SAM/proposals/2026-06-06_nexus_brief_schema.md` — schema spec unchanged this pass; long-term home should move to NEXUS-owned dir once Will/NEXUS coordinate.

**Boot-impact:**
- **Pending CLAUDE.md SPAWN PROTOCOL amendment** — brief write-back step needs to be added to closeout (likely as step 13a between docket/THESIS updates and MEMORY). Deferred this session; Will to authorize before SAM CLAUDE.md edit. Until then, brief refresh is manual / per-session-judgment.
- No other SAM boot doc changes.

**Calibration / process lessons (transferable, candidates for auto-memory):**
- **PROME-pair → NEXUS-ratify → Will-arbitrate is a healthy schema-iteration org template.** Two PROME review rounds caught the Type A/Type B distinction (the load-bearing reframe); NEXUS-as-consumer added 6 implementation-level amendments PROME couldn't generate without the consumption perspective; Will resolved the one substantive disagreement (drop-rule) decisively. Each tier added value the others couldn't.
- **"Reference, don't restate" is the anti-drift rule that lets distributed docs scale.** Brief format mandates anchor-references to PREDICTIONS.tsv preamble + red/ + THESIS for failure patterns / counter-frames / structural pillars rather than restating content. Restated content silently forks from canonical; references keep single-source-of-truth intact.
- **Single SENDING table without drop-rule is a discipline bet, not a structural fix.** NEXUS's drop-row concern was real (stale archive within 4-6 sessions). Will's call (single table + closeout discipline) puts the freshness load on the agent. If SAM brief shows stale SENDING rows over the next 3-4 sessions, the drop-rule pushback comes back — instrument informally.

---

## 2026-06-02 (AM) — KOYOMI spec amended: BASELINE AUDIT (step 2a) + CALIBRATION decline-memory

**Trigger:** Run-4 surfaced ~months-old structural exclusion in CATALYSTS.tsv — prior runs had cherry-picked super-long JGB auctions (30Y/20Y/40Y) and silently dropped 2Y/5Y belly/front. Gap only caught because Will + SAM directed KOYOMI to *investigate* the Jun 2 10Y miss vs just backfill it. Root cause: spec's add-upcoming rubric biased toward extending-from-precedent rather than re-baselining-against-source.

**Amendment (developed via teams-mode SendMessage round-trip with KOYOMI agent `aa47880ebecec2ad7`):**
- **New step 2a in § THE JOB** — propose-only baseline audit, fires on (i) monthly: first run of new calendar month → full audit; (ii) post-miss: SAM flags resolved event absent from forward TSV → release-class audit. Skip if neither triggers.
- **New § BASELINE AUDIT subsection** — universe table (MOF JGB all tenors, BOJ MPM, FOMC, Tokyo+National CPI, GDP, trade balance, Tankan, US CPI; excludes weekly auto-pulled telemetry MOF ITS + CFTC COT), execution rubric (read CALIBRATION first → fetch source → diff vs TSV → propose delta to PENDING → append confirmed dates to RELEASES.md).
- **Decline-memory mechanism** — KOYOMI reads `KOYOMI_MEMORY ## CALIBRATION "Declined release classes"` (read-only; SAM owns) before each audit, excludes declined classes from proposal list. Convergence over time (declined classes don't nag monthly); reactivation when SAM clears CALIBRATION entry.
- **READ-SET item 7a** — MOF JGB auction calendar fetch on audit triggers only (not routine).
- **RELEASES.md write extension** — every source-fetched date that becomes a TSV-proposal row must also be appended to Confirmed dates (net positive RELEASES.md contribution regardless of SAM apply decision).
- **DONE guard + RETURN block line** — BASELINE AUDIT line added to return template; DONE doesn't require audit if trigger didn't fire.

**Files touched:**
- `AGENTS/SAM/docket/KOYOMI.md` — step 2a inserted; § BASELINE AUDIT added; READ-SET item 7a; RELEASES.md OWNED-WRITE-SET bullet extended; DONE bullet added; RETURN block line added.
- `AGENTS/SAM/docket/KOYOMI_MEMORY.md` — Run-4 "coverage policy" PENDING cleared (self-resolved by amendment); Run-4 "FOMC Jul 28-29 promote" PENDING cleared (Will approved promotion → applied to TSV/CALENDAR); Run-4 "MOF schedule full-coverage default" STANDING MONITORS bullet removed (redundant per spec).

**Not done yet (propose-to-seed):** `KOYOMI_MEMORY.md ## CALIBRATION` section. The amendment references it but doesn't pre-scaffold an empty section. SAM seeds when first declination happens — structure proposed by KOYOMI: `### Declined release classes` (date + reason per line) + optional `### Accepted proposals` (pattern-tracking). Placement: between `## STANDING MONITORS` and `## NEXT RUN HINTS`.

**Boot-impact:** none for SAM. KOYOMI runs gain monthly audit cycle (~5-10 min) starting first run of July 2026; post-miss trigger is reactive only. No SAM boot doc changes.

**Calibration / process lessons (transferable, candidates for auto-memory):**
- **Teams-mode SendMessage earns when task is iterative + context-leveraging** — KOYOMI held its own spec + proposal + memory in-context across two rounds; re-spawning would have re-paid the prime cost twice. Synchronous spawn appropriate for batch propose-only single-turn work; SendMessage appropriate for refinement loops. Bias caught: defaulted to "act now" mental model the first round, missed teams-mode value — corrected on round 2.
- **Sub-agent specs need baseline-scope audits, not just incremental-update rubrics.** Any sub-agent whose job is "maintain a set" (catalysts, KB rows, trade triggers) is at risk of extending-from-precedent rather than re-baselining-against-source. The propagation bug is silent — only surfaces on direct investigation.

---

## 2026-05-29 (PM) — boot audit re-run + boot.py fetch-timeout fix (CPI/MOF/CFTC)

**Trigger:** Will-requested re-audit of the boot process after the day's doc changes. Two classes of finding — doc staleness (fixed) and a boot.py script-failure root cause (fixed).

**Doc-staleness fixes (cross-doc consistency, same class as the 5/29 AM audit):**
- `THESIS.md` PREDICTIONS section said "6 FAILED with lessons" — stale after SAM-15 resolution; corrected to **8 FAILED**, added the new failure cluster + a pointer to `PREDICTIONS_ARCHIVE.md`.
- `CLAUDE.md` didn't know `PREDICTIONS_ARCHIVE.md` existed — added a FILES-table row + a boot-step-6 note (so a future SAM resolving a prediction finds the archive and doesn't re-bloat inline `Notes`). This is the loop-closer that keeps target (b)'s slimming durable.

**boot.py CPI-failure root cause (the "why" Will asked for):** `cpi_japan.py` makes **two** e-Stat calls, each with a **30s** urllib timeout (≈60s worst case), colliding with boot.py's **60s** per-script subprocess ceiling (`run_script`, boot.py:65). On a transiently slow API the script ran up against the ceiling and surfaced as FAIL — even though it's *designed* to fall back to cached TSV. Standalone it's instant/green; only a slow-network boot trips it.
- **Fix:** lowered urllib timeout **30s→8s** (cpi_japan.py). Worst case ~16s, well under the ceiling; the cached-TSV fallback now runs. **Confirmed by boot.py re-run: Japan CPI OK 2.5s** (was FAIL 57.2s).
- **Same pattern in two more scripts** surfaced on the re-run (MOF Weekly Flows FAILed at 28.8s): `mof_flows.py` + `cftc_jpy.py` both had 30s single-call timeouts. Lowered **30s→10s** (matches the already-reasonable 15s in jgb_yields/jgb_auctions). NOTE: unlike CPI, MOF/CFTC `return 1` on fetch failure (no cached fallback) — so the 10s fix makes them fail *fast* (honest "couldn't refresh") rather than pass; the cached-fallback design choice (issue 2) was deliberately NOT changed (a loud FAIL on a dead endpoint beats silently showing stale flow data as refreshed).
- Today's MOF/CFTC FAILs were transient afternoon network flakiness (both green standalone: MOF 1.5s, CFTC 0.2s). `thresholds.py` 33s slowness is yfinance (third-party), left alone.

**Boot-impact: positive** — fetch scripts now fail fast (≤16s) instead of hanging ~30-60s; boot stays within budget and FAILs become honest signals, not timeout artifacts. All three scripts py_compile clean.

---

## 2026-05-29 (PM) — boot-slimming target (b): PREDICTIONS post-mortems → calibration archive

**Trigger:** continuation of Will's boot-slimming focus (MEMORY NEXT SESSION #2, target (b)). Will chose option (i) — keep a one-line lesson inline per closed row, move blow-by-blow to an archive.

**The problem it fixes:** closed-prediction `Notes` fields carried verbose post-mortems (8 FAILED + SAM-25 resolved-special ≈ 1,240w) that duplicate the load-bearing one-liners already in the scoreboard preamble. Boot step 6 reads the **preamble**, not the per-row blow-by-blow — so the depth was paying boot-token rent for nothing.

**Fix (no analytical/view change — logged HERE not CHANGELOG):**
- **New file `thesis/PREDICTIONS_ARCHIVE.md`** (archive-next-to-active-doc convention) — full post-mortems for the 8 FAILED rows (SAM-08/14/15/17/18/19/20/22) + SAM-25, moved **verbatim** (lossless), one `## SAM-NN` section each. Reference-only; not loaded at boot.
- **Compressed each closed row's `Notes` to a one-line lesson + anchor pointer** (`→ PREDICTIONS_ARCHIVE.md#sam-NN`). Row keeps its falsifiable record (date / confidence / outcome / one-line lesson).
- **Preserved 100%:** the scoreboard preamble (the load-bearing calibration layer per boot step 6); all **OPEN** rows (SAM-21/23/24/26 — live); all **CONFIRMED** rows (already short, and their "why" isn't duplicated in the preamble).
- Header pointer added to PREDICTIONS.tsv.

**Verify-before-archive:** lossless by construction (verbatim move, not delete); confirmed all 9 closed Pred_IDs present in the archive + TSV column integrity intact (20 data rows, all 9-col except the pre-existing 8-col SAM-13).

**Boot-impact: positive** — PREDICTIONS.tsv 2,481→1,741 words (−740 / ~30%). Combined with target (a), this session removed ~1,050 words from the cold-boot footprint. Full calibration depth one pointer away.

---

## 2026-05-29 (PM) — boot-slimming target (a): condensed THESIS deferred-Channel-1 detail

**Trigger:** continuation of Will's boot-slimming focus (MEMORY NEXT SESSION #2, target (a) — highest-ranked cut).

**The problem it fixes:** Channel 1 is DEFERRED under v1.5, yet its legacy v1.0-v1.4 mechanism depth (THESIS lines 38-86 — full Mechanism bullets, "Evidence it's happening NOW", "Evidence FLOWS at BASE pace", verbose Hedge-Ratio + Private-Credit paragraphs) carried ~25% of THESIS. A deferred channel shouldn't dominate boot doc #1.

**Verify-before-archive (same discipline as the 5/29 AM TIMELINE pass):** confirmed all three detail blocks are captured in `research/outputs/` before cutting — hedge-ratio 44.4% verbatim in `NORINCHUKIN_CLO_CONTAGION.md:71`; private-credit holdings ($45B central, Sumitomo $10.7B, Nippon TCW $3.25B, $10.1B cascade) in `JAPAN_INSURER_PRIVATE_CREDIT_EXPOSURE.md`; flow-scenario dollar/timeframe defs in `LIFE_INSURER_UST_DEEP_DIVE.md:20-22`.

**Fix (no analytical/view change — version held at 1.5, so logged HERE not CHANGELOG):** collapsed lines 38-86 into a compact "Deferred mechanism reference" bullet block with research pointers. **Preserved live-status content:** v1.5 verdict / demotion / what-still-works / what's-deferred (untouched); the **Lifer Long-End Abandonment** subsection (DOMESTIC JGB 30Y/40Y mechanism explicitly KEPT-LIVE in v1.5); the **78/18/4 flow-scenario weights** (current v1.5 view). GPIF "not a forced seller" note retained as a parenthetical. Section sub-headers promoted to `####` for structure.

**Boot-impact: positive** — THESIS 267→235 lines, 4125→3646 words (−479 words / ~11.6%). No live numbers lost; deferred depth one pointer away in `research/outputs/`.

---

## 2026-05-29 (AM) — boot-file staleness audit: THESIS live-values → STATUS pointers (doc-ownership cleanup)

**Trigger:** Will-requested audit of boot-up files for stale/unhelpful content.

**The problem it fixes:** the May 28 Tokyo-CPI downgrade (SAM-21 ~57%→~50%; carry probs 62/80→58/77) was propagated to STATUS / TIMELINE / PREDICTIONS / CHANGELOG / CALENDAR last session but **NOT THESIS** — so boot doc #1 (THESIS) contradicted boot doc #2 (STATUS) on the single most load-bearing number (June BOJ probability). A fresh SAM anchored on the stale ~57–70% before STATUS corrected it.

**Fix (no analytical/view change — version held at 1.5, so logged HERE not CHANGELOG):** replaced hardcoded live probabilities/levels in THESIS with **pointers to STATUS** (the daily-snapshot owner), per the OUTPUT RULES doc-ownership table — so they can't re-rot on the next print. Touched: one-liner (June BOJ prob), Channel 2 current-probability block + CFTC paragraph + Post-Apr-28 anchor, Channel 2 triggers (~70%), OIL-IN-YEN "Current state" (was frozen at **Brent $107.84 / May 21** — ~$16 stale), forward CATALYST table (pruned resolved May 28-29 Tokyo CPI row; trimmed 159.41/-102K/$93.13 live leaks; SAM-21 ~57%→pointer), CROSS-AGENT → HENRY (62/80) + → HAWK ($93.13).

**Also this pass:** TIMELINE + PREDICTIONS header dates bumped to 5/29; **SAM-15 flagged OPEN — FOR REVIEW** (oil-in-yen-forces-repatriation @80%; premise complicated by Phase-1-inversion finding + Brent collapse + Big-3 foreign-book growth — needs dedicated reassessment, see MEMORY NEXT SESSION); MEMORY date-stamp incident note pruned; two findings promoted to auto-memory; CLAUDE.md SIGNAL_INTAKE version ref v1.4→v1.5.

**Boot-impact: positive** — removes a boot-doc contradiction on the June BOJ probability; future CPI prints update STATUS only, THESIS stays correct via pointer.

---

## 2026-05-28 (PM, session #6) — self-calibration + provenance added to fxy_options.py (RR scale fix)

**Rebuild note:** session #6 originally implemented this but crashed before commit (window lost, no push). The crashed diff was unrecoverable; this is a clean reconstruction from the approved spec. A handful of parameter choices the original session made could not be recovered and were re-derived here — flagged `[RECONSTRUCTED]` in code for SAM review. Foundation (session #5 / `fabf645`) was fully committed and intact; only this enhancement layer was lost.

**The problem it fixes:** the FXY-proxy 25d RR has no meaningful absolute scale (runs ~10x steeper than OTC USD/JPY RR), so a raw −5.76 can't be read against the framework's OTC −0.3/−0.7 thresholds. Fix = **calibrate each reading against its OWN trailing history** (Option B; OTC-scale mapping (C) and a real CME/OTC feed (E) were rejected as gated/overkill for a confirmation signal).

**`scripts/fxy_options.py` — additive, fail-safe:**
- **Self-calibration:** `_headline_rr_series()` rebuilds the one-reading-per-date headline RR series from the TSV; `calibrate_rr()` reports the current RR as a z-score + raw deviation vs its trailing mean. While priors < `MIN_HISTORY` (8) it shows `building history (n/8)`; it activates automatically as weekly snapshots accumulate — no future session or external data needed. **Load-bearing read is DIRECTION:** z below norm = call/yen-strength demand intensifying (thesis-side); **z above norm = RR drifting toward zero = long-yen positioning UNWINDING (the genuine early-warning).**
- **Provenance:** 2 new TSV cols `Method_Ver` + `Vol_Quality` (14→16). `Method_Ver` tags the compute method so a future math change can't silently contaminate the trailing series (calibration only mixes same-version readings). `Vol_Quality` grades each reading (ok / approx / rr_na / none); only ok+approx feed calibration. `_ensure_schema()` pads + backfills legacy rows (stamps existing RR readings with current version + quality). `append_tsv` upsert extended to backfill the 2 new cols.
- **Reconstructed params (SAM-reviewable):** `MIN_HISTORY=8` (from the "(n/8)" spec floor), `CALIB_WINDOW_DAYS=60` ("60-day average"), `METHOD_VER="fxy-proxy-v1"`, `Vol_Quality` bucket thresholds, z-score (vs simple delta) as the primary readout, and column order (appended at end).

**Validation:** py_compile clean; idempotent on re-run; migrates the live 53-row / 14-col TSV to 16-col and stamps the 4 existing 5/28 readings as `fxy-proxy-v1 / ok`. Self-cal currently reports `building history (1/8)` — only one date of RR history exists, exactly as expected. No new deps (math stdlib). **Boot-impact: safe** (additive, fail-safe; degrades to raw RR when history is short).

**Deferred:** STATUS.md unchanged — self-cal is in `building` state, no z-score signal to surface yet. Add a STATUS self-cal line once history crosses 8 readings.

---

## 2026-05-28 (PM, live session #5) — FXY-derived vol proxy built into fxy_options.py (closes the CVOL/RR gap)

Built the vol-signal feed that recon (#3) parked. Decision trail: CME CVOL route gated → fall back to a **free proxy computed from the FXY options chain `fxy_options.py` already pulls.** Placement settled with Will: *data* is workbook-native (it's a scripted feed) but the *signal* is STATUS; so raw lands in FXY_OPTIONS.tsv, the read lands in STATUS, and this **retires the 3 VX vol rows**.

**`scripts/fxy_options.py` — additive + fail-safe** (compute wrapped in try/except; can never break the boot sweep):
- `compute_iv_skew()` returns **ATM IV** (CVOL proxy: IV at nearest-spot strike ×100) + **25d RR** (BS-delta via `math.erf`, no scipy; finds ~25Δ OTM call/put). Both per-expiry → term structure.
- **SIGN convention (the crux):** FXY is inverse to USD/JPY, so RR reported as `IV(FXY put) − IV(FXY call)` = USD/JPY-convention (negative = FXY calls bid = yen-strength demand = thesis-side). Documented in code + VOL_OPTIONS_FRAMEWORK.md.
- **SCALE caveat:** FXY ETF skew runs far steeper than OTC RR — framework's −0.3/−0.7 OTC thresholds DON'T transfer. `_rr_flag` reads sign/direction only (NOT the OTC "stress/crisis" labels — caught + fixed during validation when a raw −5.76 was mislabeled "crisis"). `_iv_flag` keeps the §1 CVOL bands as a soft guide.
- Headline = expiry nearest 30 DTE (mirrors CVOL horizon). Spot fallback added (t.history if .info flaky).
- **TSV:** 2 new cols `ATM_IV_pct`, `RR25_USDJPY` (12→14). One-time `_ensure_schema()` migration pads historical rows. `append_tsv` rewritten as an **idempotent upsert** (adds new rows; backfills IV/RR on existing blank rows; self-heals partial pulls) — needed because today's rows predated the feature.

**`scripts/boot.py`:** added "VOL PROXY"/"ATM IV"/"25d RR" to the collapse-filter `key_markers` so the vol read surfaces in the default (non-verbose) brief when fxy runs (RR line uses ↓→↑ arrows, not stoplight emoji, so it needed explicit markers).

**`STATUS.md`:** 2 new market-table rows (ATM IV + 25d RR) — the live signal surface.

**`VX.tsv`:** retired 3 vol rows (12.00/12.01/12.03) — superseded by FXY_OPTIONS.tsv (raw) + STATUS (read). **VX now 3 rows** (wage ×2 + trade balance), all awaiting their own scripts → VX on a path to dissolution, as predicted.

**`VOL_OPTIONS_FRAMEWORK.md`:** DATA SOURCES updated (proxy = primary feed; CME/OTC = gated reference); added a "FXY-DERIVED VOL PROXY" section documenting method, sign, scale caveat.

**Validation:** live-pulled 2026-05-28 — spot $57.65 ✓; ATM IV term structure 8.01%(Jun)→13.28%(Dec); RR −5.76/−5.58/−5.99 across liquid Jun/Sep/Dec (thin Jul −1.46 = noise) → consistent steep call skew = real thesis-side positioning. py_compile clean; idempotent on 2nd run; --print OK; all 53 TSV rows uniform 14-col. **First read: calm IV level + heavily thesis-side skew** = directional long-yen positioning without imminent-vol pricing. No new deps (yfinance/pandas already used; math stdlib). **Boot-impact: safe** (additive, fail-safe; boot skips fxy if today's row exists).

**Deferred:** insurers/<name>.md retire-vs-refresh; CLAUDE.md FILES-table touch-ups (FXY_OPTIONS new cols, VX scope, FLOW_ARCHIVE — eval-baseline-gated); RR proxy could later add a "vs 20d avg" trend once history accumulates.

---

## 2026-05-28 (PM, live session #4) — KB.tsv superseded-row move + v1.5 scan + archive/ graveyard cleanup

Closed out the workbook audit (Will's "finish the workbook"). Three parts:

**1. Moved 4 SUPERSEDED rows KB.tsv → KB_ARCHIVE.tsv** (KB 123→119 lines; ARCHIVE 52→56). Rows already carried v1.5 supersession notes: `081` Nippon repatriation-risk, `084` Meiji ESR-non-disclosure, `087` Meiji UST/3-6mo-timeline, `092` Sumitomo sell-at-159 mean-reversion. All boot-safe (no script reads KB).

**2. v1.5 consistency scan (LIVE rows):** verdict — KB is in good shape; v1.5 was already well-propagated in the earlier 2026-05-28 KB cleanup (the `KB-172` synthesis row + numerous `RECONCILED 2026-05-28` notes). Two unambiguous data-staleness refreshes applied: `KB-127` (Inflection-2 scenario repointed from dead 'April hike' → Jun 16) and `KB-135` (30Y-10Y spread refreshed 131bp Feb-8 → ~117bp May-27). Per-insurer Feb-8 "repatriation risk/timeline" rows (091/095/097/099/101…) carry stale framing but are globally caveated by `KB-172` — individual rewrite folds into the deferred `insurers/<name>.md` retire-vs-refresh decision; NOT touched here.

**3. archive/ graveyard cleanup (Will: trash 5 scaffolding + 2 superseded .md):** verified STAGING content fully integrated (STAGING_B industry data → KB-059/062; STAGING_A SK-refiner → KB_ARCHIVE ×12) before deleting. **Trashed (gio trash) 7 files:** KB_STAGING_A/B(.md + _FORMATTED.tsv), KB_BACKUP_10rows.tsv, FRAMEWORK_IMPLEMENTATION_FEB11.md, INSURER_UST_TRANSMISSION_ANALYSIS.md (superseded by research/outputs/LIFE_INSURER_UST_DEEP_DIVE.md). **Kept as deep archive:** ML.tsv (master session log — only copy), VX_HISTORY.tsv (threshold time-series), SAM_WORKBOOK.xlsx (legacy Excel master).
> 🔧 **RE-POINTED 2026-08-14 (PROME prune-scan 8/12, FALSE_PRESERVATION).** All three "kept" files were later deleted by **`c819a955c`** (2026-06-30, *"cut 0-ref archives (track A)"*) — **not** by the 6/30 prune `1cb18fbc3`, and **not** by this 5/28 pass. `workbook/archive/` **does not exist on disk.** The "only copy" flag on `ML.tsv` now resolves to **git history only**: recover with `git show c819a955c^:AGENTS/SAM/workbook/archive/ML.tsv` (verified present 8/14 — 3 files at that tree: ML.tsv · VX_HISTORY.tsv · SAM_WORKBOOK.xlsx). The root archive's `ML_ARCHIVE_2026-01.tsv` is a **different file** — not a substitute. *Superseded text above preserved verbatim per the remedy riders.*

**Files:** KB.tsv (119 rows), KB_ARCHIVE.tsv (56 rows), 7 archive/ deletions. **Boot-impact: none.**

**Workbook audit COMPLETE** (sessions #2–#4): FLOW refresh-split ✅, VX slim-to-unique ✅, KB superseded-move + scan ✅, archive cleanup ✅. **Remaining deferred (not workbook-hygiene):** vol IV/skew proxy build in fxy_options.py (queued — CME route gated); insurers/<name>.md retire-vs-refresh; CLAUDE.md FILES-table touch-ups (FLOW_ARCHIVE add + VX scope narrow — defer, eval-baseline trigger).

---

## 2026-05-28 (PM, live session #3) — workbook VX.tsv slim-to-unique + CVOL/RR source recon

Third-pass workbook cleanup (Will's "get the workbook caught up" review). VX.tsv was a 37-metric threshold dashboard built Feb–Apr, BEFORE boot.py existed — newest row 45 days stale (Apr 13). Confirmed **no script reads VX.tsv** (grep scripts/ clean) → edit boot-safe. Walkthrough found ~85% of rows were duplicated by sources that post-date VX: auto-pulled feeds (JGB_YIELDS, USDJPY, CFTC_JPY, CPI, FXY_OPTIONS, MOF_FLOWS, JGB_AUCTIONS), STATUS KEY THRESHOLDS, insurers/TRACKER, research docs — and 8 rows actively contradicted v1.5 (insurer "selling", MOF "regime-change" repatriation, war-era PROME scenario probs).

**Decision (Will): slim to unique rows only** — VX repositioned as a small "manual-only metrics not yet auto-pulled" sheet. **37 → 6 rows.**

- **Kept + REFRESHED to current data (3 macro, not auto-pulled):** `8.03` Nominal Wage (Mar 2026 +2.7%, cooled from Feb +3.3% → ORANGE→YELLOW); `8.04` Real Wage (Mar +1.0%, decelerating from +1.9%); `11.02` Trade Balance (Apr 2026 **¥+301.9B surplus**, beat — old oil-shock-deficit Phase-1 framing did NOT materialize; Brent collapsed).
- **Kept, FLAGGED stale pending build (3 vol):** `12.00` Vol Convergence composite, `12.01` CVOL, `12.03` 25d Risk Reversals — VX's one genuinely-unique contribution (CVOL + RR are not auto-pulled, not in STATUS).
- **Dropped 31 rows** (no physical archive — duplicates of live auto-pulled series / v1.5-superseded / resolved; full pre-slim original preserved in git at prior commit). `12.02` FXY Call OI dropped — now covered by auto-pulled FXY_OPTIONS.tsv.

**CVOL/RR source recon (Will: "build a pull, recon first"):** No clean free direct source — CME CVOL EOD API is license-gated (~$290/mo sub-vendor, no confirmed free tier); CBOE JYVIX discontinued (Yahoo ^JYVIX = zeros); 25d RR only via paid Refinitiv/Bloomberg/Saxo. **Viable free path identified:** extend existing `fxy_options.py` to compute a 30d ATM-IV proxy (CVOL-equivalent) + 25d skew proxy (call-IV − put-IV = risk-reversal-equivalent) from the FXY options chain it ALREADY fetches via yfinance. Proxy (FXY-ETF options, not USD/JPY OTC) but free/scriptable/zero-auth. **Build decision pending Will** — not yet built.

**Files:** `workbook/VX.tsv` (37→6 rows). **Boot-impact: none.** **FILES-table note:** CLAUDE.md line ~236 VX description should narrow to "manual-only un-scripted metrics (wages, trade balance, vol-signal)" on next CLAUDE.md pass (defer — eval-baseline trigger). **FLOW_ARCHIVE.tsv** add to FILES table also still pending (from session #2).

**Deferred workbook passes remaining:** KB.tsv 4 SUPERSEDED rows → KB_ARCHIVE + v1.5 consistency scan; archive/ scaffolding cleanup (KB_STAGING_*, KB_BACKUP_10rows, ML.tsv + VX_HISTORY.tsv, SAM_WORKBOOK.xlsx). Plus NEW: vol IV/skew proxy build in fxy_options.py (if Will green-lights).

---

## 2026-05-28 (PM, live session #2) — workbook FLOW.tsv refresh-split (v1.5 consistency)

Second-pass workbook cleanup, triggered by Will's "get the workbook caught up" review. FLOW.tsv (14 transmission-flow vectors) was ~7 weeks stale (last touched Mar 4 – Apr 7) and actively **contradicted v1.5** — most dangerously logging carry-unwind probs at 80/95/95 (vs current 12/62/80) and Channel 1 as "CRITICAL-CONFIRMED, $10-15B/mo selling active NOW" (v1.5 demoted Channel 1 to deferred after 3-of-3 benign Big 3 ESR prints). Pre-step confirmed **no script reads FLOW.tsv** (boot.py only auto-pulls data feeds) — edit is boot-safe. Mirrors the May-28 KB.tsv live-vs-archive split pattern.

**Split 14 rows → 10 live (`FLOW.tsv`) + 4 archived (new `workbook/FLOW_ARCHIVE.tsv`).**

- **Archived (resolved point-in-time telemetry):** `5.03` Path D (Apr 23-24/May 1 BOJ hike window — resolved by Apr 28 hold), `6.01` Energy→JGB Supply (March QatarEnergy/LNG crisis — abated), `6.03` War Escalation (Apr-7 8pm Hormuz deadline — passed, Brent $110→$92), `7.01` Taiwan LNG→TSMC (Mar-15 inflection — passed, cross-domain non-core). Each preserved verbatim with a `[RESOLVED YYYY-MM-DD: …]` prefix in Key Insight + Status → `ARCHIVED (was …)`.
- **Refreshed to v1.5 (5 live vectors):** `5.02` Carry Unwind (probs 80/95/95→12/62/80; CFTC -72.9K→-93,905; USDJPY→159.21; repointed to Jun 16 single-path); `2.03` J-SOLV (CRITICAL-CONFIRMED→DEFERRED; 3-of-3 benign ESR, foreign books growing; J-ICS long-end leg kept INTACT); `5.01` Floating Mortgage (repointed to Jun 16 collision); `3.01` CLO/Norinchukin (flagged Jun FY2025 print as the data-refresh gate; Apr-7 figures marked PENDING REFRESH); `1.06` Fiscal Doom Loop (re-pointed from stale "Feb 19 20Y auction" to current super-long auction softness + Jun 16).
- **Reaffirmed (5 structural, date-touch + "(Reaffirmed 2026-05-28, v1.5)" tag):** `1.05` Rural Political, `3.02` Desperation Swap, `3.03` Private Market Contagion, `4.01` BDC Latent, `6.02` USD-vs-Yen Safe-Haven (spot refreshed to 159.21).

**Files:** `workbook/FLOW.tsv` (14→10 rows, all v1.5-consistent); `workbook/FLOW_ARCHIVE.tsv` (new, 4 rows, same 10-col schema). Both verified 10-col clean. **Boot-impact: none.** **FILES-table note:** CLAUDE.md line ~236 lists FLOW under hand-maintained workbook tsvs — add FLOW_ARCHIVE alongside it on the next CLAUDE.md pass.

**Deferred workbook passes remaining (unchanged):** VX.tsv keep-vs-retire (decide-after-review pending); KB.tsv 4 SUPERSEDED rows → KB_ARCHIVE + v1.5 consistency scan; archive/ scaffolding cleanup (KB_STAGING_*, KB_BACKUP_10rows, ML.tsv + VX_HISTORY.tsv, SAM_WORKBOOK.xlsx).

---

## 2026-05-28 (PM, live session) — KOYOMI first run + `RELEASES.md` + spec hardening (prototype validated)

Operationalized the KOYOMI prototype created earlier today (entry below). Will spawned KOYOMI for the first time as a **named/persistent teammate** for a shakedown run. Outcome: prototype validated — Will likes the pattern; KOYOMI is now operational.

**First run earned its keep immediately:** KOYOMI caught a real **CALENDAR↔CATALYSTS.tsv divergence** — CALENDAR was missing 6–7 forward events the TSV already had (FOMC Jun 17, US CPI Jun 10, both JGB auctions, GDP revision Jun 8, National May CPI Jun 19, Tokyo June CPI Jun 26). She reconciled CALENDAR up to the TSV, then surfaced 3 design questions instead of guessing. Will decided all 3.

**Three decisions encoded into `docket/KOYOMI.md`:**
1. **TRUTH MODEL (split ownership)** — new spec section. `CATALYSTS.tsv` = source-of-truth for the dated-event SET (which events, dates, priority); `CALENDAR.md` = source-of-truth for narrative/routing/threshold prose; **neither carries live spot.** Resolves the "which file wins" ambiguity that made KOYOMI second-guess.
2. **Prune by the >1-week retention rule, not on sight** — codified in JOB step 1. A resolved event leaves the *forward* views when its date passes but stays in RECENTLY RESOLVED until >1 week old. (KOYOMI's own round-1 instinct; my spawn-prompt instruction to prune May 26 early was wrong — she correctly held it.)
3. **Strip live spot from CALENDAR** — executed by KOYOMI round 2.

**New file — `docket/RELEASES.md`:** recurring-releases reference. Cadence rules (CFTC=Fri/data-as-of-Tue, Tokyo CPI=last Fri, GDP 2nd prelim=~3wk after 1st, BOJ/FOMC/JGB-auction cadence) + official schedule links (ESRI, MIC, BOJ, MOF, CFTC, Fed, BLS) + a "Confirmed dates" scratchpad. Now KOYOMI's first stop for date verification (WebSearch only if this can't resolve). Holds **schedules only — no analysis, no live data.**

**`KOYOMI.md` spec changes:** added TRUTH MODEL section; read-set expanded to include RELEASES.md + both docket files (they were listed only under write-set); JOB step 1 (prune rule) + step 3 (no spot refresh) rewritten; granted a narrow write-set exception (append-only to the RELEASES.md "Confirmed dates" table when a date is verified at source).

**`docket/CALENDAR.md` — spot stripped (KOYOMI):** removed all live levels from INTERVENTION WATCH, PHASE 2 WATCH, STRUCTURAL CHANNEL 1 MONITORS, GEOPOLITICAL WATCH, and the May 29 CFTC / Jun 10 JGB auction rows — kept structural thresholds + significance, replaced bare-level cells with "see STATUS". **Historical levels in RECENTLY RESOLVED left intact** — they're resolved-event *outcome records* (what printed), not live monitors duplicating STATUS, and age out under the 1-week rule. SAM-confirmed convention: the strip rule applies to forward monitors, not outcome records.

**Jun 8 GDP date:** web-verified cadence-consistent (Q1 1st prelim May 19 + ~3wk → Mon Jun 8); logged ⚠️ in RELEASES.md pending ESRI schedule confirmation. Row kept in CALENDAR + TSV, noted "(date cadence-derived; confirm at ESRI)".

**Git:** SAM stages all docket changes (KOYOMI does not commit, per agent-git-isolation). **Boot-impact:** none — `catalyst_countdown.py` runs clean; CALENDAR is slimmer (one less divergence surface, no daily spot treadmill). **Eval note:** today's CLAUDE.md SPAWN PROTOCOL change (docket path + KOYOMI step 10) is a standing eval re-baseline trigger — flagged to Will.

---

## 2026-05-28 (AM) — new `docket/` folder + KOYOMI sub-steward (delegation prototype)

Created `AGENTS/SAM/docket/` to co-locate the forward-calendar layer and give a future maintenance sub-agent a single, enforceable ownership boundary. Outcome of a design conversation with Will: SAM stays sole orchestrator + analyst; bounded *busy-work* (calendar/catalyst upkeep) gets delegated to an ephemeral, SAM-internal sub-steward so SAM's context stays free for judgment.

**Moves (git mv, history preserved):**
- `CALENDAR.md` → `docket/CALENDAR.md`
- `workbook/CATALYSTS.tsv` → `docket/CATALYSTS.tsv`

**Repaths (verified both scripts resolve the new path + parse correctly):**
- `catalyst_countdown.py` — CATALYSTS path → `docket/`; docstring updated.
- `jgb_auctions.py` — added `DOCKET` const; CATALYSTS path → `docket/` (AUCTIONS_TSV stays in workbook/). Confirmed `load_catalyst_auction_dates()` still finds the 2 JGB auctions.
- `boot.py` untouched (invokes scripts by name).

**CLAUDE.md updated:** boot step 3 (`docket/CALENDAR.md`); write-back step 10 (sync CALENDAR + CATALYSTS, prefer spawning KOYOMI for sizeable refresh); doc-ownership table (added CATALYSTS row); FILES table (docket/CALENDAR + docket/CATALYSTS + docket/KOYOMI rows); corrected the old line-233 inaccuracy (CATALYSTS/FLOW/VX were wrongly listed as "auto-pulled" — now split auto-pulled vs hand-maintained). Forward-pointing CALENDAR refs updated in TRADE/STRATEGY/THESIS; historical mentions + CHANGELOG history left as-is.

**KOYOMI brief — `docket/KOYOMI.md`:** SAM-internal sub-steward (暦, "almanac"), spawned on command, NOT a network peer. Read-set: STATUS / THESIS§CATALYST / TIMELINE + run catalyst_countdown.py. Exclusive owned write-set: `docket/` only. Job: prune resolved, add upcoming, refresh stale content, keep CALENDAR↔CATALYSTS in sync + ISO/auction-name format rules. **Escalate-don't-act clause** is the load-bearing guardrail: anything analytical goes back to SAM, never edited inline. Does not commit (git is SAM's). Returns a tight summary.

**Status: command-first prototype.** KOYOMI runs only when SAM/Will invokes it — evaluate-mode until Will decides he likes the pattern. **Deferred (graduation rungs):** boot-time staleness *tripwire* in catalyst_countdown.py (runway < ~10d → auto-nudge SAM to spawn KOYOMI) → weekly scheduled run (needs an external firer — PROME/cron; `/loop` only runs within a live session). Boot-impact: none.

**Remaining deferred workbook passes (unchanged):** VX.tsv keep-vs-retire; FLOW.tsv refresh-vs-archive; archive/ scaffolding cleanup.

---

## 2026-05-28 (later) — CATALYSTS.tsv refresh + live-search additions + countdown holiday-skip (deferred-pass #1: KEEP, not retire)

Resolved the first deferred next-pass item from the KB cleanup entry below. The deferred note read "CATALYSTS.tsv retire (dup of CALENDAR)" — **corrected after gap-check: the file is not a free delete.** `scripts/catalyst_countdown.py` (runs at boot) READS CATALYSTS.tsv as its structured countdown feed. CALENDAR.md's dates are freeform ("Thu-Fri May 28-29", "🔴🔴 Tue Jun 16", "Early Jun", "Ongoing" triggers) and can't be parsed reliably into the strict `%Y-%m-%d` the script needs. Re-plumbing the script to read CALENDAR is fragile/intrusive.

**Decision: KEEP CATALYSTS.tsv as the machine-readable forward-event feed; CALENDAR.md remains the human-readable narrative/routing doc.** Different consumers. The root problem was drift (hand-maintained, ~6 weeks stale — still listed resolved May 1/14/15/20/22 events, Jun 16 BOJ row stale at SAM-21 70% / swap 74%), not duplication per se.

- Rewrote forward-only: dropped 6 resolved May events; refreshed to current v1.5 forward set — Tokyo May CPI (5/29), CFTC weekly (5/29), BOJ MPM base case (6/16, SAM-21 ~57% / market 55-65%, SAM-24 25bp @85%), Sato board (6/16), BOJ interim QT (6/16), May trade balance Phase 1 lag-test (6/18). who_cares + threshold_signal columns synced to current routing.
- Verified `catalyst_countdown.py` runs clean against refreshed file: imminent Tokyo CPI + CFTC (1 trd), upcoming Jun 16 cluster + Jun 18 TB. Boot-impact: none (positive — countdown was previously showing only stale Jun 16 with wrong probabilities).

**Live-search catalyst additions (Will-approved):** ran web research (MOF / Fed / BLS / Stats Bureau / Cabinet Office) for missing forward catalysts; added 7 rows, all dates verified at source. **FOMC Jun 17 (🔴)** — the rate-differential half of the carry trade, was absent (file tracked only the BOJ side); lands 24h after BOJ Jun 16 and now co-headlines the HIGH-PRIORITY summary. Also: US CPI May (Jun 10, 🟠, feeds FOMC dots); JGB 30Y auction (Jun 10, 🟠, direct J-ICS long-end / SAM-26 demand test); Japan Q1 GDP 2nd est (Jun 8, 🟡); JGB 20Y auction (Jun 25, 🟡); National May CPI (Jun 19, 🟡 — verified off Stats Bureau raw table, NOT Jun 26); Tokyo June CPI (Jun 26, 🟡). File now 13 forward events, date-sorted.

**Script fix — catalyst_countdown.py holiday-skip:** `trading_days_between` previously counted all weekdays; now skips a HOLIDAYS frozenset (Japan national holidays + US market holidays, 2026). Market-agnostic union (errs ~1 day toward "more urgent" near a single-market holiday — documented in-code). Verified: Jun 18→Jun 25 now 4 trd not 5 (skips Juneteenth); July 4 week skips correctly. Extend the set each calendar year.

**Anti-drift recommendation (NOT yet done — needs Will sign-off):** tie CATALYSTS.tsv refresh to CALENDAR.md maintenance so it can't drift again — either (a) add a one-line reminder to CLAUDE.md write-back step 10 ("update CALENDAR.md → also refresh workbook/CATALYSTS.tsv dates for catalyst_countdown.py"), or (b) leave as-is and refresh CATALYSTS opportunistically at boot when stale. Also: CLAUDE.md FILES table (line ~233) inaccurately lists CATALYSTS among tsvs "auto-pulled by boot.py" — it is hand-maintained and READ by boot, not written. Flag for the CLAUDE.md pass.

**Remaining deferred workbook passes:** VX.tsv keep-vs-retire (STATUS dup; ~6wk stale); FLOW.tsv refresh-vs-archive (Feb-Apr war/LNG content); archive/ scaffolding cleanup (KB_STAGING_*, KB_BACKUP_10rows, ML.tsv + VX_HISTORY.tsv merge, SAM_WORKBOOK.xlsx).

---

## 2026-05-28 — workbook KB.tsv cleanup: split + recategorize + internal backfill

Two-batch cleanup of `workbook/KB.tsv` (was 167 rows, frozen at 2026-04-07). Triggered by Will's workbook-staleness review. Pre-step verified **no script reads KB.tsv** (boot.py only auto-pulls the data feeds) — schema change is boot-safe.

**Batch 1 — split + recategorize:**
- Split 167 rows → 116 live (`KB.tsv`) + 51 historical (new `workbook/KB_ARCHIVE.tsv`). Historical = resolved point-in-time operational telemetry (SK-refiner saga, Mar-27 USD/JPY-160 intervention sequence, dated carry-probability snapshots, FY2025-end window timing).
- Consolidated 32 inconsistent Category values → 9 (Insurer / Regulatory / Repatriation / BOJ-Wages / Carry-FX / Energy / Household / Framework / Cross-Agent). Live rows grouped by category, sorted by ID within.
- Added `Status` column (LIVE / SUPERSEDED / HISTORICAL).
- Flagged 4 insurer assessments contradicted by v1.5 actuals as SUPERSEDED **in place** (KB-081/084/087/092) with actual outcomes appended — preserves the threshold-vs-mechanism calibration lesson rather than burying it.

**Batch 2 — dedup + internal backfill (no web; sourced from STATUS / TIMELINE / TRACKER):**
- Merged duplicate KB-148 into KB-137 (identical +50bp→ESR-200% calc, DEEP_DIVE §1B).
- Added 7 LIVE rows (KB-168..174) closing the Apr-7 → May-28 sync gap: BOJ Apr 28 hold + 3-way dissent; April CPI dovish miss; MOF interventions Apr 30 + May 6; Big 3 FY2025 ESR actuals (3-of-3); FY2026 plan outcomes (zero clean foreign-bond cuts); current vol/positioning; and **SYNTHESIS KB-172** resolving the KB-164 (active-at-stress-pace) vs KB-081 (deferred) Channel-1 contradiction in favor of deferral.
- KB-166/167 left archived as superseded forecasts; their outcomes captured in new LIVE rows instead of un-archiving.

**Batch 3 — numeric-conflict reconciliation (Notes-only appends, rows stay LIVE):**
- **RESOLVED — JGB losses → ¥13.2T** ($86B, Jun 2025; FY2025 prints confirm worsening: Nippon -¥5.73T, Meiji -¥2.16T). Annotated KB-063/064; the ¥9T DEEP_DIVE figure was earlier/lower.
- **RESOLVED — hedge ratio → 44.4%** (Mar 2025, 14-yr low; STATUS/TRACKER). Annotated KB-065/066; DEEP_DIVE's ~30% was too low, RP-SAM-4's 45-50% range was right.
- **STANDING GAP — per-insurer UST split** ($450-810B) not closeable from FY2025 disclosures (no clean UST line). Annotated KB-061/062/139/140 with the Japan all-inst TIC total ($1,239.3B Feb 2026) + rotation-within reframe.

**Net: KB.tsv 167 → 122 live rows. Boot-impact: none.** Calibration framing: the "blind spot" was a sync gap, not lost intelligence — current state was already in STATUS/TIMELINE/TRACKER; KB had drifted.

**Deferred to next workbook passes:** CATALYSTS.tsv retire (dup of CALENDAR); VX.tsv vs STATUS owner decision; archive scaffolding cleanup (KB_STAGING_*, SAM_WORKBOOK.xlsx, ML.tsv + VX_HISTORY.tsv merge).

---

## 2026-05-27 evening — v1.5 propagation sweep (STRATEGY, TRADE, TRACKER, RED, all 7 insurer profiles)

Same-day evening follow-up to the morning v1.5 thesis bump. Will flagged STRATEGY.md + TRADE.md as likely stale; I confirmed and asked to expand to a full doc-stack audit. Outcome: 12 docs refreshed across decision layer, RED counter-thesis layer, and per-insurer reference layer. Triage discipline: ranked by behavioral impact per [[feedback_audit_behavioral_ranking]] before touching files.

**Triggering trail:** Morning STATUS+THESIS+CHANGELOG resolved Position A (Sep $60 OTM) as NOT WARRANTED under v1.5 single-path. But STRATEGY.md + TRADE.md still presented full entry rules + ranked entry windows for the same Position A — a behaviorally-active contradiction (future SAM or Will reading those would get conflicting guidance from STATUS vs decision docs). The Sep-$60-NOT-WARRANTED reframe is the load-bearing edit that drove the whole sweep.

**Files touched (12 total):**

1. **`STRATEGY.md`** — v1.4 → v1.5; Stage 3 reframed multi-channel → single-path; hard trigger table refreshed (SAM-21 70%→~57%, ESR row ✅ resolved 3-of-3 benign, JGB 30Y retracement noted, Channel 3 dormant); **Position A flipped AUTHORIZED → NOT WARRANTED** with 4 explicit re-activation conditions; When-to-HOLD refreshed; Key Check Dates pruned forward-only; new CHANGELOG entry. Live data references redirected to STATUS.md.

2. **`TRADE.md`** — header v1.5; Tranche 2 Hard-Trigger Status table SAM-21 + ESR row + Channel-3-dormant + JGB-30Y-retracement; Position A NOT WARRANTED with re-activation conditions; Carry Unwind Probability synced to v1.5 (12/62/80); Risk Factors restructured (BOJ-delay 10%→25% single-path elevation; oil 20%→15%; intervention-fails 15%→12%; new Channel-1-reactivation row at 10%); "Bigger Hike" section anchored to SAM-24 @85%; Watchlist EWJ + Japan Banks SAM-21 refs; Key Dates pruned forward-only; Catalyst Sequence collapsed to TIMELINE pointer.

3. **`insurers/TRACKER.md`** — header 5/26 PM → 5/27 v1.5; Channel 1 banner "🟡 DOWNGRADED, NOT DEAD (Day 1)" → "🟡 DEFERRED STRUCTURAL BACKSTOP (3-of-3 confirmed)" with 5 explicit reactivation conditions; Sumitomo row in ESR table fully populated (197% ↑+19pt, foreign book +¥1.11T detail, Symetra/Dearborn); "Reading the Big 3 mutual prints" closed out as 3-of-3 RESOLVED with v1.5 signature table (insurer × ESR × mechanism × foreign book × US direction); "Wed Sumitomo pattern-confirmation test" section retired; Industry aggregates JGB row updated (30Y 3.866% / 40Y 3.836% / 10Y 2.713%); "What we're waiting for" pruned + added H2 FY2026 plans as next structural re-test; Key Dates Sumitomo ✅; Phase 2 inception extended to May 27 with Brent $93.13 + MOU framework hardening.

4. **`red/COUNTER_THESIS.md`** — full rewrite v1.0 → v1.5. New one-liner: single-path narrowing = thinner not stronger; June BOJ is most-priced event of cycle. Explicit calibration credit for CH-002 (FY2025 net buying) and CH-003 (intervention spike-and-reverse) wins driving v1.5 demotion. New narrative builds on threshold-vs-mechanism trap potentially repeating on Channel 2 (BOJ stress absorbed via targeted long-end op, not rate hike). "What world looks like if I'm right" / "What would prove me wrong" re-spec'd for v1.5. Explicit "what I'm NOT challenging" section preserves [[feedback_red_edge]] discipline. v1.0 counter-thesis archived below for historical record.

5. **`red/CHALLENGES.md`** — full rewrite. Resolved CH-002 + CH-003 (CONFIRMED) and CH-006 (DISMISSED) removed and logged. Retargeted CH-001 (severity 🟠→🟡 under v1.5 — Channel 1 demoted), CH-004 (severity 🟠→🟡 — lower probabilities, less false-precision risk), CH-005 (unchanged under v1.5), CH-007 (severity 🟡→🟠 — single-path makes consensus risk worse). **NEW CH-008 — Fiscal-Dominance Frame (BOJ Frozen, Not Hike-Ready) from eval Case 02 baseline runner; resolves Jun 16.** This formalizes the v1.5.x candidate finding logged in morning MEMORY into an active RED challenge with counter-evidence and resolution criteria.

6. **`red/LOG.md`** — new calibration scoreboard at top (2 CONFIRMED, 1 DISMISSED, 4 RETARGETED, 1 NEW). 5/27 resolution rows for CH-002, CH-003 (CONFIRMED) and CH-006 (DISMISSED) with full evidence trails. Retarget rows for CH-001 / CH-004 / CH-005 / CH-007 with v1.5 reasoning. New CH-008 entry. Original 3/31 rows preserved with cross-references — full audit trail intact. Major calibration call surfaced: **RED's CH-002 (FY2025 was net buying) was correct in substance 8 weeks before v1.5 demotion landed** — durable evidence that RED earns its keep.

7-13. **`insurers/<7 profiles>.md`** — all 7 refreshed under v1.5 (decision point in CLAUDE.md "retire-vs-refresh deferred post-Sumitomo" resolved as REFRESH after Will pushed back on the retire recommendation):
   - **nippon-life.md** — FY2025 ESR 195% section with Resolution Life decomposition; canonical threshold-vs-mechanism trap example; Stancorp attribution error fixed (Stancorp is Meiji's, not Nippon's)
   - **meiji-yasuda.md** — FY2025 ESR 208% manageable; pre-FY2025 "ESR NOT DISCLOSED red flag" resolved; cleanest base-case datapoint of Big 3
   - **sumitomo.md** — FY2025 ESR 197% ↑+19pt with full asset-composition table (foreign book +¥1.11T); Symetra/Dearborn detail; explicit cross-ref to RED CH-002 confirmation; most narrative-rich of the three
   - **dai-ichi.md** — FY2025 ESR ~220% +10pp equity-rally-driven; framed as least-representative of Big 4 / US-PC-stress amplifier via Canyon Partners
   - **norinchukin.md** — positioned as standalone independent Channel 1 reactivation gate (Jun FY2025); CEO Kitabayashi public risk-off concern preserved; ¥500B Q1 "fastest on record" decline
   - **fukoku.md** — first-mover historical-marker; J-ICS DOMESTIC mechanism precedent case (preserved in v1.5)
   - **japan-post.md** — clean-read JGB seller (zero PC); CEO Sahara Mar-3 directional-right / timing-wrong (April expectation missed); v1.5 sentiment confirmation for BOJ hike thesis

**Pattern preserved across all 7 profile refreshes:** durable per-insurer narrative (executive quotes with attribution, specific deal commitments by amount/counterparty, source attributions, historical trajectory) kept intact. The refresh added FY2025 ESR data + v1.5 framing on top, didn't strip the depth layer. Per Will's pushback: "TRACKER's table form can't hold executive quotes / PC deal specifics / source attributions" — refresh-not-retire was the right call.

**Net behavioral fix:**
- Position A NOT WARRANTED resolution now coherent across STATUS, STRATEGY, TRADE (was split before this sweep)
- RED has a functional counter-thesis targeting v1.5 again (was targeting v1.0, useless for v1.5 single-path decisions)
- Per-insurer reference layer + TRACKER aggregator layer now both reflect 3-of-3 Big 3 ESR window resolution
- Future SAM boots will load consistent v1.5 framing across all 12 docs

**Boot impact:** None directly — STRATEGY/TRADE not in boot sequence; TRACKER not in boot sequence; RED not in boot sequence; per-insurer profiles not in boot sequence. All are reference docs read on demand. Boot.py + boot docs (THESIS, STATUS, CALENDAR, TIMELINE, MEMORY) untouched.

**Cross-session lesson promoted to auto-memory:** `finding_refresh_not_retire_perentity_profiles.md` — when a thesis bump leaves per-entity profiles stale, refresh-with-trajectory-preservation beats archive-and-rely-on-aggregator. Aggregator files (TRACKER-style table) cannot hold executive quotes / source attributions / deal specifics / historical trajectory. Transferable to CARL (per-bank profiles?), REGINALD (per-name?), HENRY (per-vol-product?), BROCK (per-spread-pair?), HAWK (per-belligerent?).

---

## 2026-05-27 afternoon — eval suite v1 → v1.1 (split-file redesign after baseline contamination)

Same-day follow-up to the v1 scaffold below. Will ran the baseline against v1 single-file cases and reported both responses showed near-verbatim phrase echo from EXPECTED criteria. Diagnosed by a sister model (Prome / external session) and confirmed: v1 design had INPUT + EXPECTED + DO-NOT in a single file, README told operator to paste only the INPUT block, but file-design discipline is stronger than operator-instruction discipline. Will pasted the whole file (or selection scrolled past rubric), and rubric language leaked into the runner's prompt.

**Smoking gun:** Case 02 response contained "super-long duration adds proportionally more solvency-capital strain than the yield pickup compensates for" — that exact phrase was in v1's EXPECTED list, NOT in the INPUT. Near-verbatim echo confirms contamination source.

**Substantive finding (positive):** Both responses also contained reasoning that was NOT in EXPECTED — positioning recommendations, BOJ-tactical paths, FX rate-diff decoupling explanations. Real reasoning was happening alongside the rubric echo. v1 just couldn't measure how much.

**v1.1 fix (same-session ship):**
- Split each case into TWO files. `case_NN_<topic>_INPUT.md` is pasteable (scenario data + questions only). `case_NN_<topic>_RUBRIC.md` is scorer-only with a prominent "⚠️ SCORER ONLY — DO NOT PASTE INTO RUNNER" header. Makes contamination physically harder.
- Re-shaped EXPECTED criteria from quote-form to assertion-form. Case 02 J-ICS solvency-strain criterion rewritten as "Explains why super-long is structurally unattractive under J-ICS — beyond just citing J-ICS by name. Must connect duration repricing to solvency capital impact AND explain why this dominates yield-pickup motivation. Wording is flexible. The test is whether the response articulates the structural disincentive, not whether it uses any particular phrase." Tests concept, not phrasing match.
- Added contamination self-check at multiple points in INPUT file headers ("Does your selection contain `EXPECTED`, `DO NOT`, or `RUBRIC`? → too much"). README repeats the check. RUBRIC files include a post-response contamination-signature check.
- Added `PASS-CAVEATED` and `FAIL-CONTAMINATED` result categories to scoring rubric.

**Files in v1.1 (active):**
- `evals/README.md` — rewritten for v1.1 split-file workflow, includes v1 → v1.1 baseline-finding note
- `evals/case_01_nippon_esr_INPUT.md` + `evals/case_01_nippon_esr_RUBRIC.md`
- `evals/case_02_jgb30y_jics_INPUT.md` + `evals/case_02_jgb30y_jics_RUBRIC.md`
- `evals/results.tsv` — 2 baseline rows logged as PASS-CAVEATED with contamination diagnosis
- `evals/baseline_artifacts/` — preserved v1 response transcripts (docx) for audit trail

**Files removed:**
- `evals/case_01_nippon_esr_mechanism.md` (v1 combined-file)
- `evals/case_02_jgb30y_jics_direction.md` (v1 combined-file)

Both files were never committed to git in their v1 form, so deletion is clean (no rewrite-history issue).

**Recommendation for next session:** re-baseline against v1.1 once. Pick Case 02 — the harder of the two to derive unprompted (structural-inversion call against pre-J-ICS muscle memory) — for the higher-diagnostic-value clean run.

**Boot impact:** None. `evals/` remains operator-only infrastructure.

---

## 2026-05-27 morning — eval suite v1 (scaffold) [SUPERSEDED — see v1.1 above]

Ship-day for the SAM eval suite. New top-level `evals/` directory with 2 frozen-scenario test cases. Origin: design-doc review session with Will (Ideas.docx walked through 4-part infra menu; eval suite picked as highest-ROI item; scoped to 2 cases not 5 per discipline-of-cap-on-first-ship).

**v1 artifacts (now superseded by v1.1):**
- `evals/README.md` — runner protocol (skip-boot pattern), pass/fail scoring rubric, re-run cadence, retire policy, failure-protocol diagnostic buckets.
- `evals/case_01_nippon_esr_mechanism.md` — combined INPUT + EXPECTED + DO-NOT in one file. **Contamination flaw discovered same-day; redesigned in v1.1.**
- `evals/case_02_jgb30y_jics_direction.md` — same structure, same flaw. **Redesigned in v1.1.**
- `evals/results.tsv` — header row only initially; v1.1 added 2 baseline-PASS-CAVEATED rows.

**CLAUDE.md update:** FILES table entry added for `evals/` between `red/` and `research/outputs/`. Explicit note: SAM does NOT auto-load eval files at boot — eval scoring happens in a separate fresh skip-boot session that Will runs.

**Runner pattern (skip-boot):** Will opens a fresh Claude Code session in `AGENTS/SAM/`, pastes ONLY the INPUT block (which contains explicit "DO NOT RUN BOOT" framing), scores the response against EXPECTED + DO-NOT, appends to `results.tsv`. CLAUDE.md + auto-memory auto-load (that's correct — they contain the lesson surface; the test is application not derivation). STATUS / THESIS / PREDICTIONS / TIMELINE do NOT load (they contain answer keys for resolved cases — would contaminate the test).

**Cap discipline:** v1 holds at 2 cases. No case 3 until either (a) one of the first 2 catches a regression, OR (b) a new lesson emerges that neither covers. Per README.md retire policy: cases retire when their lesson migrates to script-enforcement.

**Boot impact:** None. `evals/` is operator infrastructure, not agent context.

---

## 2026-05-26 evening (continued) — MEMORY restructure + CLAUDE.md audit + scripts fixes + cpi_japan.py build

Same-evening continuation of the folder cleanup logged below. Five additional workstreams, six commits total.

**MEMORY.md restructure (commit 0e58c525):** 87→44 lines. Promoted threshold-vs-mechanism lesson (SAM-25/26) + audit-behavioral-ranking lesson to auto-memory (`finding_threshold_vs_mechanism.md`, `feedback_audit_behavioral_ranking.md`). Compressed Session Notes to template (terse LAST SESSION + numbered NEXT SESSION); retired PENDING + INFRASTRUCTURE STATUS sub-sections. Findings 7→2 (kept SAM-operational items; retired 2 stale — PROME SCRATCH contradicts `project_openclaw_prome_degraded`, EUR/JPY operationalized in boot.py). References collapsed 5→2 lines.

**CLAUDE.md audit (commit 20da4862):** 228→233 lines but net more accurate. Phase A (SPAWN PROTOCOL): fixed broken "All mail lives in removed:" line; added ⚠️ messaging-overhaul status note pointing to `[[project_messaging_overhaul]]`; boot step 6 now references PREDICTIONS calibration scoreboard + `[[finding_threshold_vs_mechanism]]`; boot step 14 captures auto-memory promotion path. Phase B: deleted WAR — TWO-PHASE JPY DYNAMIC section (contradicted THESIS v1.4 supply-destruction-inverted Phase 1 framing); removed stale "Current" column from KEY THRESHOLDS table; added 4 thresholds (USDJPY <130-135, JGB 10Y >2.40%, MOF weekly >¥1.5T). Phase C: added Big 3 ESR <200% via market stress row to CROSS-AGENT SIGNALS (mechanism-aware per TRACKER); retired Shunto row (annual reactivation note); cleaned blank-section debris; FILES table now lists MAINTENANCE.md, SIGNAL_INTAKE.md (with stale warning), expanded workbook breakdown beyond just VX.tsv.

**Scripts fixes (commit a4572223):**
- `jgb_auctions.py` — TSV-append bug fixed. Climate Transition uniform-price auctions lack weighted-average column, causing `TypeError: unsupported format string passed to NoneType.__format__` at append time. Added `_fmt()` helper handling None gracefully. Verified by appending May 25 5-Year Climate Transition (BTC 4.622x). Boot 7/8 → 8/8 green.
- `usdjpy.py` — added `TOUCH_TOLERANCE = 0.10` constant; modified `days_since_level()` to use tolerance band. May 6 low 155.05 now correctly registers as touching 155 (was n/a previously). Added intraday-range alert as third summary line — `INTRADAY_RANGE_WARN = 2.5` 🟠, `INTRADAY_RANGE_CRIT = 4.0` 🔴, calibrated against Apr 30 (5.15y) + May 6 (2.84y) intervention events. Would have correctly flagged Apr 30 as INTERVENTION-GRADE.
- `AUTOMATION_PLAN.md` — status banner DRAFT → ✅ EXECUTED with verification line.

**cpi_japan.py — net new boot script (commit bdca2519):** 9th script in boot sequence; closes the Japan CPI observability gap that was previously hand-pulled via web search. Architecture: e-Stat API v3 (`api.e-stat.go.jp/rest/3.0`), statsDataId `0003427113` (2020-base CPI), pulls headline + core + core-core YoY for National (area 00000) + Tokyo Ku-area (13A01). `ESTAT_APPID` loaded from repo-root `.env` (gitignored). Two-table threshold scheme per Will's `Thresholds.md` note — separate buckets for Core (BOJ target series) and Core-core (trend gauge), plus cross-series divergence flag (≥0.5pp = energy/subsidy driven; ≤0.2pp = broad-based softening), plus Tokyo-vs-National comparison note with CALENDAR `<1.95%` Tokyo trigger adjustment. Idempotent `workbook/CPI.tsv` append on (Series, Reference_Month). Today's read: 🟠 National Apr 2026 core 1.4 Soft band + 0.5pp divergence (energy/subsidy-driven softness BOJ can look through); Tokyo gap to National 0.0pp vs typical -30-40bp (softness may be closing). Boot 9/9 green, 9.9s total. Will registered the AppID; one-time setup. Pattern carries forward to future Japan-stats scripts (BOJ, trade balance, employment).

**Boot impact:**
- `boot.py` BOOT_SEQUENCE: 8 → 9 entries (added "Japan CPI" between MOF Weekly Flows and Catalyst Countdown).
- `MAINTENANCE.md` and `SIGNAL_INTAKE.md` (with stale warning) now listed in CLAUDE.md FILES table.
- `KEY THRESHOLDS` in CLAUDE.md no longer carries stale Current values; STATUS.md is the canonical live values doc.
- `workbook/CPI.tsv` — new file, 12 rows seeded (Nov 2025 → Apr 2026 × National + Tokyo).
- Repo-root `.env` — new file, gitignored, holds `ESTAT_APPID`.

**Auto-memory entries created:**
- `finding_threshold_vs_mechanism.md` — falsifiable-prediction discipline pattern (SAM-25/26 both fired the same trap)
- `feedback_audit_behavioral_ranking.md` — rank doc-cleanup findings by behavioral impact, not line-count

---

## 2026-05-26 evening — Folder cleanup Pass 1a/1b/2a/2c (Will-directed audit response)

**Trigger:** Will asked for folder-structure audit (post-Sumitomo pre-watch session). Audit surfaced ~6 weeks of accumulated dead-ends at SAM's edges; Will approved Pass 1a + 1b + 2a + 2c (deferred 2b insurer per-name files until post-Sumitomo; deferred Pass 3 research/ reorg).

**Pass 1a — dead top-level dirs trashed:**
- `recon/` (single Mar 15 file) — `git rm`
- `domain/` (single Mar 17 file, superseded by `research/outputs/LIFE_INSURER_UST_DEEP_DIVE.md`) — `git rm`
- `sources/` (3 Mar 17 files) — `git rm`
- `session_archive/` (single Mar 3 STATUS archive) — `git rm`

**Pass 1b — stale top-level files:**
- `LAST_COMPLETION.md` (Apr 11 stale; absorbed by MEMORY.md "LAST SESSION" block) — `git rm`
- `SIGNAL_INTAKE.md` (Apr 8 stale; thesis now v1.4) — added top-banner `⚠️ STALE` note pointing readers to THESIS/STATUS as canonical; file preserved for WALTER routing reference pending messaging-system overhaul decision

**Pass 2a — workbook staging moved to workbook/archive/:** ⚠️ **`workbook/archive/` is GIT-HISTORY-ONLY as of 2026-08-14** — the 7 staged files below were trashed 5/28 after verify-integration (disclosed at the 5/28 entry above); the remaining 3 were cut by **`c819a955c`** (6/30, *"cut 0-ref archives (track A)"* — **not** `1cb18fbc3`). Full 10-file tree recoverable at `git show 52724b88a:AGENTS/SAM/workbook/archive/<file>`; the 3 survivors also at `c819a955c^:` (both verified 8/14).
- `KB_STAGING_A.md`, `KB_STAGING_A_FORMATTED.tsv`, `KB_STAGING_B.md`, `KB_STAGING_B_FORMATTED.tsv` (Mar 30 unresolved staging)
- `KB_BACKUP_10rows.tsv` (Mar 30)
- `ML.tsv` (Mar 17), `VX_HISTORY.tsv` (Mar 17)
- Live `workbook/` now shows only the 10 active tsvs (CATALYSTS, CFTC_JPY, FLOW, FXY_OPTIONS, JGB_AUCTIONS, JGB_YIELDS, KB, MOF_FLOWS, USDJPY, VX) + archive/

**Pass 2c — inbox/outbox bankruptcy (one-time sweep per `project_messaging_overhaul`):**
- *Inbox* — 7 files trashed after read-review. None held uncaptured signal: 2 info-only WALTER routes (IMF GFSR, Baker Hughes), 2 absorbed-into-thesis claims (Hormuz exposure, oil products inventory), 1 falsified claim (Japan UST-selling — Feb TIC contradicts), 1 tangential (equity rotation), 1 sweep superseded by Apr 30 + May 6 intervention integration.
- *Outbox* — 2 Apr-era files trashed (6+ weeks stale, undelivered, superseded); 3 May 21 files moved to `delivered/` (recent, content preserved); current May 26 PROME tracker_cleanup_complete left in `outbox/`.

**Files touched (`AGENTS/SAM/` only):**
- Trashed: `recon/`, `domain/`, `sources/`, `session_archive/`, `LAST_COMPLETION.md`, 7 inbox files, 2 Apr-era outbox files
- Moved: 7 workbook staging files → `workbook/archive/` *(⚠️ **that directory no longer exists — git-history-only since `c819a955c` 6/30**; see the re-pointer at Pass 2a above. Recovery: `git show 52724b88a:AGENTS/SAM/workbook/archive/<file>`)*; 3 May 21 outbox files → `outbox/delivered/`
- Edited: `SIGNAL_INTAKE.md` (banner), `MAINTENANCE.md` (this entry)

**Boot impact:**
- `ls AGENTS/SAM/` now shows 7 top-level docs (was 9) + 9 subdirs (was 12 incl. dead). Cleaner orientation surface.
- `ls workbook/` now shows live tsvs only; archive subdir holds the staging graveyard.
- `inbox/` empty (processed/ unchanged); `outbox/` shows only current session's work.
- No boot-sequence file path changes — all paths in CLAUDE.md boot steps unaffected.

**Deferred:**
- Pass 2b (insurers/<name>.md per-insurer profiles) — wait for post-Sumitomo Wed AM when Big 3 mutual state is fully resolved; then retire-vs-refresh decision is cheaper.
- Pass 3 (research/ reorg into outputs/+archive/) — cosmetic, low behavioral impact, defer indefinitely.
- SIGNAL_INTAKE full refresh — pending messaging-system overhaul direction.

**Rationale (per [[feedback_audit_behavioral_ranking]] / 2026-05-26 lesson):** Cuts ranked by behavioral impact, not line-count. HIGH-impact dead dirs and stale top-level files cleared first; MED-impact workbook staging + inbox/outbox cleared because user opted in; LOW-impact research/ reorg deferred.

---

## 2026-05-26 PM — TRACKER.md mechanism-aware routing + Channel 1 banner + staleness fixes (PROME cleanup ask + follow-up audit)

**Trigger:** PROME signal `prome_2026-05-26_insurer_tracker_cleanup_request.md` — Will + PROME walked SAM domain to understand Channel 1; flagged stale alert rule ("ANY ESR <200% → 🔴") and missing mechanism-vs-threshold discrimination. Independent finding from same root as MEMORY 2026-05-26 (threshold-vs-mechanism trap on SAM-25). Follow-up audit (post-PROME-reply) caught two additional actively-wrong sections.

**Change (single-file structural cleanup, two passes):**

*Pass 1 — PROME ask:*
- Added top-level **🟡 CHANNEL 1 STATUS** banner ("downgraded, not dead") above the J-ICS Key Insight. Captures: what's intact, what's deferred (not dead), why the old rule is too crude.
- **Signal routing replaced** — old 5-bullet rule list collapsed; new 5-row mechanism-aware table discriminating market-loss-driven vs M&A-driven sub-200% prints. New row for J-ICS-cited super-long avoidance.
- **"What's confirmed"** — re-ranked by mechanism evidence weight. Oct 2025 50% planned-cut survey explicitly down-weighted as superseded by Apr 2026 actuals (zero clean cuts). Old "Nippon 222% → if drops <200% → tone changes" assertion stripped as superseded by May 26 Nippon 195% (M&A) outcome.
- **"What we're waiting for"** — refreshed: Sumitomo Wed May 27, mid-tier Late Jun, Norinchukin Jun, any explicit reduction target (Fukoku-2023-style), MOF ITS sustained selling.
- **KEY DATES** — added Apr 14-25 FY2026 plans (✅) and May 22 CPI (✅ dovish miss) with outcomes. Refreshed Sumitomo row to call out M&A-vs-stress pattern test explicitly.
- **MONITORING CHECKLIST** — section header retired (week mostly resolved); extract-checklist preserved inside the new SIGNAL ROUTING section. Added US-subsidiary direction-of-travel row (Resolution Life, Stancorp).
- **Last Updated + Purpose** banners refreshed.

*Pass 2 — follow-up staleness fixes (Will-approved after Pass 1 audit):*
- **Industry Aggregates JGB rows refreshed.** JGB 30Y was claiming "4.000% ✅ BREACHED" as if durable; STATUS already showed 3.931% (May 22, retraced -7bp). Replaced with breach-and-retrace narrative + footnote treating 4.000% as structural stress level, not durably-held floor (SAM-26 lesson). JGB 10Y refreshed 2.770% May 20 → 2.749% May 22. JGB 40Y row added (3.921%).
- **Oil-yen section replaced.** "Apr 12 Hormuz blockade context" was v1.3-era framing ("oil spike → trade deficit widens → yen weakens → FX gains paper over bond losses") — actively wrong post-v1.4. April trade balance posted ¥+302B SURPLUS (blockade collapsed import volumes); CPI missed on fuel subsidies; Brent has since collapsed -12% on MOU optimism. Replaced with tight v1.4 oil-yen note flagging Phase 1 inversion + Phase 2 inception + insurer FX-cushion fading, pointing to `thesis/THESIS.md` § OIL-IN-YEN as single source of truth.

**Files touched:**
- `insurers/TRACKER.md` (+58 / -51 net across both passes; structural replacement, not accumulation)

**Boot impact:** None on the standard 7-step read sequence. TRACKER is read on insurer-specific spawns. Behavioral impact is twofold: (1) alert-routing correctness — future ESR-threshold breaches won't auto-trigger 🔴 if the mechanism is capital action; (2) cross-doc consistency — TRACKER no longer reports JGB stress facts in conflict with STATUS, and no longer carries an obsolete mental model of the oil-yen channel.

**Convention transferable (Pass 1):** Threshold-based alert rules across SAM (and other agents) should be audited for mechanism qualifier — the "level breach → route as stress" reflex mis-fires when capital actions, M&A, or sub-debt drives the breach. Apply when calibrating BROCK HY OAS triggers, REGINALD KRE bear-line, HENRY VIX regime triggers — any level-based signal where the same level can be reached by multiple mechanisms.

**Lesson reinforced (Pass 2):** Doc-cleanup asks benefit from a follow-up audit pass after executing the explicit scope — the PROME ask covered the rule + Channel 1 banner + key dates, but the two highest-impact remaining issues (cross-doc fact conflict on JGB 30Y; obsolete oil-yen mental model) were *adjacent* to the ask, not in it. Catching them required a fresh end-to-end read once the requested edits were in. Behavioral-impact ranking (per MEMORY 2026-05-26): only proposed top-2 of 11 noticed items; deferred cosmetic and duplicative items. Validates "rank by behavioral impact first, line count second" lesson in practice.

**Not changed (per PROME scope):**
- `STATUS.md` — Channel 1 demotion already reflected on May 26 AM (line 14)
- `thesis/THESIS.md` — v1.5 reframe deferred to post-Sumitomo
- `thesis/CHANGELOG.md` — no analytical version change; this is rule calibration + staleness, not thesis update

**Completion note:** filed to `outbox/2026-05-26_to-PROME_tracker_cleanup_complete.md` (Convention B own-outbox routing).

---

## 2026-05-26 — TIMELINE archive split + `thesis/timeline/` folder

**Trigger:** Boot-doc audit found `thesis/TIMELINE.md` at 555 lines / 56KB — 45% of total boot context. Resolved entries going back to Mar 31 + obsolete v1.3-era forward-looking sections were padding the read.

**Change:**
- Created `thesis/timeline/` folder.
- Split content at cut date 2026-05-11 (v1.4 era inception, Bessent-Katayama meeting).
- Active post-May-11 narrative + pending branch points → `thesis/timeline/TIMELINE.md`.
- Pre-May-11 resolved events + obsolete v1.3 forward sections + historical Branch Point rows → `thesis/timeline/ARCHIVE.md` (reverse-chron, prepend-newest pattern).
- Trashed old `thesis/TIMELINE.md`.

**Files moved/created:**
- NEW `thesis/timeline/TIMELINE.md` (~220 lines)
- NEW `thesis/timeline/ARCHIVE.md` (~190 lines)
- NEW `MAINTENANCE.md` (this file)
- REMOVED `thesis/TIMELINE.md` (trashed)

**Path refs updated:**
- `AGENTS/SAM/CLAUDE.md` — 3 path references (boot step 4, write-back step 12, Files table)
- `AGENTS/SAM/red/CLAUDE.md` — 1 path reference (boot step 2)

**Boot impact:** TIMELINE read 555 → ~220 lines (-60%). Total boot context ~1,230 → ~890 lines (-28%).

**Convention established (per Will):** archives co-locate with active docs; root `archive/` is legacy-graveyard only.

**Next maintenance candidates (audit findings from 2026-05-26):**
1. ~~PREDICTIONS archive split~~ → **REVISED + EXECUTED** (see PREDICTIONS entry below)
2. ~~THESIS de-dupe (core)~~ → **EXECUTED** (see THESIS entry below)
3. ~~STATUS narrative compress~~ → **EXECUTED** (see STATUS entry below)
4. ~~THESIS Forward catalyst table refresh~~ → **EXECUTED** (see THESIS residuals entry below)
5. ~~THESIS KEY THRESHOLDS — strip Status column~~ → **EXECUTED** (see THESIS residuals entry below)
6. ~~THESIS POSITION VIEW — collapse to pointer~~ → **EXECUTED** (see THESIS residuals entry below)

All 6 candidates executed in one sitting on 2026-05-26.

---

## 2026-05-26 — PREDICTIONS.tsv restructure-in-place (calibration-preserving)

**Trigger:** Original audit recommendation was to archive CONFIRMED/FAILED rows. Will pushed back: closed predictions are calibration gold — 6 high-confidence failures (90% / 75% / 65% / 65% / 60% / 55%) are the strongest available signal against overconfidence in future prediction-writing.

**Change (lighter than original plan — no file split):**
- Rows reordered: **OPEN → RESOLVED → FAILED → CONFIRMED**, by Pred_ID within each.
- Added `#`-prefixed preamble block at top with:
  - Calibration scoreboard (7 CONFIRMED / 6 FAILED / 1 RESOLVED-special / 6 OPEN)
  - High-confidence failures listed with one-line lesson each
  - Failure-pattern synthesis (political ceiling, flow-data interpretation, intervention prob-weighting, threshold-vs-mechanism)
  - SAM-25 called out as the threshold-vs-mechanism trap
- No rows removed. No file split. Boot step 6 still scans single file.

**Files touched:**
- `thesis/PREDICTIONS.tsv` (in-place restructure; 20 data rows preserved + 20-line `#`-preamble added)

**Boot impact:** Negligible line increase (~22 preamble lines), but boot step 6 now leads with calibration-warning instead of arbitrary historical first row.

**Convention established:** TSV files can carry `#`-prefixed comment preambles for calibration / context that humans scan but parsers skip. Use sparingly; keep under ~25 lines.

---

## 2026-05-26 — STATUS.md narrative compress (candidate #3)

**Trigger:** STATUS.md at 203 lines carried ~70 lines of prose narrative that duplicated TIMELINE (event narratives) and THESIS (channel/v1.5 framing). Per CLAUDE.md doc-ownership rule, STATUS is "snapshot format — tables and levels, minimal prose."

**Change (4 sub-edits):**
- **STATE OF PLAY (lines 5-44)** — compressed 40-line prose block to 10-line bullet headlines + pointer to `timeline/TIMELINE.md` May 26 section. Preserved the "what's TOP OF MIND today" hook.
- **REFERENCE DATA (lines 169-188)** — collapsed 8 channel-by-channel narrative sub-summaries to one-line-per-channel + BOJ QT data point. Stripped duplicates of CPI / Brent / GDP / trade balance (all in TIMELINE). Retained unique data: hedge ratio 44.4%, MOF intervention ¥10T total, BOJ QT pace.
- **Bottom THESIS section (lines 192-203)** — stripped entirely. The refreshed THESIS.md status banner already owns this; bottom STATUS restate was pure duplication. Replaced with one-line pointer.
- **In-section narratives** — light wordiness trim: probability footnote, stale "Decision-eve Tue" note (Tue had already happened), redundant "No position change May 22-25" recap.

**Files touched:**
- `STATUS.md` (203 → 153 lines, -25%)

**Boot impact:** Total boot context 1,230 → **815 lines (-34% from baseline)** across all 6 candidates.

**Discipline reinforced:** STATUS = snapshot (tables, current values, decision context). TIMELINE = narrative. THESIS = structural. Going forward: paragraphs of event-narrative in STATUS should auto-route to TIMELINE; STATUS keeps bullet headlines + pointer.

---

## 2026-05-26 — THESIS.md de-dupe

**Trigger:** Boot-doc audit found THESIS.md duplicated content owned by other files: Catalyst Sequence "Resolved" table (~25 rows narrating events that live in TIMELINE) + CONFIRMED/FALSIFIED PREDICTIONS tables (duplicating PREDICTIONS.tsv).

**Change:**
- Stripped Catalyst Sequence "Resolved (Apr 13 → May 21)" subsection (~25 rows). Replaced with one-line pointer to `timeline/TIMELINE.md` + `timeline/ARCHIVE.md`.
- Stripped CONFIRMED PREDICTIONS + FALSIFIED PREDICTIONS tables (14 rows total). Replaced with one-line pointer to `PREDICTIONS.tsv` and its preamble calibration record.
- Refreshed version banner from May 21 framing ("THESIS STRENGTHENED") to May 26 framing ("MIXED — Channel 1 weakened post-ESR, Channel 2 dominant, Channel 3 dormant"). Did NOT bump version — v1.5 reframe deferred to post-Sumitomo per MEMORY guidance.

**Files touched:**
- `thesis/THESIS.md` (276 → 235 lines, -15%)

**Boot impact:** Total boot context now 1,230 → ~846 lines (-31% from baseline) after all three 2026-05-26 cleanups (TIMELINE split + PREDICTIONS restructure + THESIS de-dupe).

**Doc-ownership reinforced:** THESIS = structural argument + thresholds + channels + conviction. TIMELINE = event narratives. PREDICTIONS.tsv = falsifiable record. Each doc now contains only what it owns; cross-doc references replace duplication.

**Forward-table staleness flagged (not executed in this pass — surfaced as candidates #4-#6 above):**
- Forward catalyst row "Fri May 22 Japan April CPI" is resolved (left in place — pointer-only de-dupe was the locked scope)
- Duplicate "Mid-June BOJ" rows
- KEY THRESHOLDS table has stale May 21 "Status" column
- POSITION VIEW says 8 shares; actual is 13

---

## 2026-05-26 — THESIS.md residual cleanups (batch #4-#6)

**Trigger:** Three staleness/duplication issues surfaced during #3 (core de-dupe) but were out of locked scope. Batched as a single follow-up pass.

**Change:**
- **#4 Forward catalyst table refresh** — dropped resolved May 22 CPI row; updated Big 3 ESR row to reflect Sumitomo-only Wed May 27 (Nippon/Meiji done); added Tokyo May CPI Thu-Fri May 28-29; merged duplicate Mid-June BOJ rows into one with SAM-21 + SAM-24 references; added pointer to CALENDAR.md for operational tracking.
- **#5 KEY THRESHOLDS — Status column stripped** — table now 2 cols (Level, Significance), purely structural. Current values + breach status redirected to STATUS.md. Removed JGB 40Y row (was definitional placeholder with no significance).
- **#6 POSITION VIEW — collapsed to thesis-level statement** — kept one-line "what we hold + why" (FXY long, target $60-62, stop $55.05). Removed stale share count (8 vs actual 13). Pointed to STATUS.md / TRADE.md / STRATEGY.md for operational details.

**Files touched:**
- `thesis/THESIS.md` (235 → 235 lines — net flat; pointer text added back what stale-content cuts removed. Win is in structural clarity, not line count. Cumulative day total: 276 → 235, -15%.)

**Doc-ownership reinforced again:** THESIS = structural (thresholds as definitions, position as thesis-level statement, forward catalysts as thesis-dependent events). STATUS = current snapshot (values, sizes, fills). CALENDAR = operational forward tracking. TRADE = position details. STRATEGY = decision playbook.

---

*Each new structural change prepends above. Older entries below.*
