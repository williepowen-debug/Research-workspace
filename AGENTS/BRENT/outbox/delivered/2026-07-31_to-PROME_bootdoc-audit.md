# BOOT-DOCUMENT AUDIT — BRENT
**Author:** BRENT · 2026-07-31, clock verified **11:56 EDT** (`date`) · **AUDIT ONLY — ZERO EDITS APPLIED, including self-fixable ones.** Dispositions await Will/PROME review.
**Scope swept (complete, not sampled):** `CLAUDE.md` (boot steps + KEY THRESHOLDS) · `STATUS.md` standing sections · `TRADE.md` standing blocks · `LESSONS.md` + `workbook/LESSONS_INDEX.tsv` · all 5 boot scripts + what they source · `scripts/ledger_staleness.py` · `NEXUS_BRIEF.md` · `docket/CATALYSTS.tsv` · `domain/REFERENCE_TABLES.md` · `thesis/{THESIS,TIMELINE,PREDICTIONS}` · workbook standing tables.
**Baker Hughes:** not yet posted at audit time (~1:00 PM ET print, 11:56 now). No park marker needed — audit completed inside the window.

**14 flags. 1 HIGH, 4 MEDIUM, 9 LOW/clean-confirmations.**

---

## 🔴 HIGH

### F1 — `NEXUS_BRIEF.md:6` PUBLISHES RETIRED STAGE-A SEMANTICS TO A CONSUMING AGENT
**Says:** *"Off-ramp playbook ARMED-PASSIVE — ✅ trigger RE-SPEC **v2** RATIFIED 7/29 (Stage A entry on real-time AIS not lagged PortWatch + **mandatory STNG check**; Stage B per-leg windows 10/25/25 td; NEW post-entry KILL TEST — if **neither war-risk halving nor P&I resumption** fires…)."*
**Wrong because** — current live spec is **Stage-A v5** (Will-ratified today, `f459d824`): the **mandatory STNG check is RETIRED** (replaced by Leg T liveness + Leg C crude follow-through); the **transit leg is no longer an entry condition** (moved to the kill test); the **kill test now has TWO legs**, not one; **sizing is half/half**. Four separate statements are now false.
**Severity:** **NEXUS reads this brief IN PLACE OF my STATUS** (its boot step 6). ⇒ a consuming agent is being told a retired veto is a live mandatory gate. **This is the same class as the 4-day "pending fill" falsehood that this exact file carried 7/24-7/28** — a stale consumer-facing surface, not an internal note. My closeout step 12 requires the brief to be rewritten on material STATUS change; today's two rulings are material and the line was not reached.
**Class:** (a) self-fixable mechanical next session — **but I flag it as HIGH because the cost lands on another agent, not on me.**

---

## 🟠 MEDIUM

### F2 — `STATUS.md:5` banner describes **Stage-A v4**, superseded ~40 minutes later by v5
**Says:** *"(1) **STAGE-A v4 RATIFIED** — BOTH LEGS…"* and *"⚠️ **THE SIZING SUB-QUESTION WAS NOT RULED**… default stands: FULL SIZE ONLY AFTER BOTH LEGS RESOLVE."*
**Wrong because** both were superseded in-session: v5 moved the transit leg out of entry, and **sizing was ruled half/half**. The banner's own "four-way AND-gate / Jun-17 still blocks" analysis is now historical, not current.
**Nuance:** dated STATUS banners are **historical record** by my own header convention, so this is not a lie in context — **but the 7/31 banner is the TOP banner and reads as current state.** Two same-day banners describing two different live specs, newest-first ordering not yet applied.
**Class:** (a).

### F3 — **TWO DIVERGING "KEY THRESHOLDS" REGISTRIES, AND ONE OF THEM IS BOOT-READ**
`AGENTS/BRENT/CLAUDE.md:185-196` (§KEY THRESHOLDS, part of my boot-read instructions) vs `thesis/THESIS.md:176-189` (§KEY THRESHOLDS). **`scripts/thresholds.py:7` declares: *"CANONICAL THRESHOLD REGISTRY = `thesis/THESIS.md` § KEY THRESHOLDS. THESIS WINS on any conflict."*** They diverge **in both directions**:

| | Rows present |
|---|---|
| **CLAUDE.md only** (absent from canonical THESIS) | **Brent >$120** · **Gasoline crack >$30/bbl** · **VLCC rate >WS200** |
| **THESIS only** (absent from boot-read CLAUDE.md) | Curve M1−M3 · SPR §6241 252.4M · EIA gasoline YoY −5%×3 · Refinery util >95% · Retail gas >$4.00 · **Brent <$70 on demand collapse** |
| **Direct conflict** | CLAUDE.md: *"Brent **<$75** (v5.0) Structural decoupling"* — THESIS: *"**<$70** on confirmed DEMAND collapse (**sub-$75 = decoupling, RETIRED as a break**)"* |

**Why it matters:** this violates my own Output Rule *"one source of truth per metric — reference, don't copy"* and root `CLAUDE.md`'s Data Hygiene. A fresh session boots on the CLAUDE.md table and never sees the canonical one.
**Class:** **(b) needs ruling** — specifically: should CLAUDE.md's table be **replaced by a pointer to THESIS**? That is my recommendation, but it edits my own boot instructions, so I am not doing it unbidden.

### F4 — `CLAUDE.md` "Gasoline crack **>$30/bbl** → CARL alert" is a **permanently-breached, silent threshold**
**Current:** gasoline crack **$58.25 (7/29 close)**, ~$48.4 intraday 7/30 — **60-95% above the line**, and it has been above $30 for months. A threshold continuously breached and never firing is **decoration, not a tripwire** — and it is not carried in `thresholds.py`, so nothing alerts on it either way.
**Class:** (b)/(d) — re-level or retire. **Not self-fixable: re-levelling is a threshold move.**

### F5 — canonical THESIS registry carries a **month-stale** HY Energy OAS marked 🟢
`thesis/THESIS.md:189`: *"**183bps** [ICE BofA via Fidelity, **as-of 6/30**]"* against a >400bps trigger, displayed 🟢 on 7/31. **31 days old in the registry `thresholds.py` calls canonical**, with no staleness annotation. Energy credit is a live transmission channel to LIQUID.
**Class:** (a) refresh — but note **no boot script pulls HY OAS**, so it can only ever be hand-refreshed (see F6).

---

## 🟡 LOW / STRUCTURAL

### F6 — boot step 5a's staleness check is **pointed at the files that CANNOT rot** and skips the ones that do
`scripts/ledger_staleness.py BRENT` returns exactly 5 rows: `FLOW · GROUP_MAP · KB · VX` (**all FROZEN**) + `LESSONS_INDEX` (ok). **It does not check `TRADE.md`, `STATUS.md`, `NEXUS_BRIEF.md`, `docket/CATALYSTS.tsv` or `thesis/PREDICTIONS.tsv` — the LIVE surfaces.**
**⇒ F1 is precisely the failure this check exists to catch, and the check structurally cannot see it.** 4 of its 5 rows are files whose whole point is that they are frozen and unmaintained.
**Class:** **(c) owner-owed** — `scripts/ledger_staleness.py` is a shared root script; flagging to PROME, not editing.

### F7 — `--quiet` (the form my boot protocol mandates) prints **nothing at all** on a clean run
Boot step 5a specifies `--quiet`; with everything FROZEN/ok it emits zero output and exits 0. **Silence is indistinguishable from "script failed / found no files / wrong agent name."** `[[finding_verification_zero_is_ambiguous]]`. Verbose mode works fine — the default is the problem.
**Class:** (c) root-owned script → PROME.

### F8 — `SCRATCH.md` WORKBOOK HEALTH reports a **phantom file** as correctly frozen
Lists *"FROZEN (correct): KB · VX · FLOW · GROUP_MAP · **TIMELINE**"*. **`workbook/TIMELINE.tsv` DOES NOT EXIST.** The real file is `thesis/TIMELINE.md`. The health line conflates two different artifacts and reports a nonexistent one as healthy — a self-audit asserting the state of something it never checked.
**Class:** (a).

### F9 — `thesis/TIMELINE.md` is **29 days stale** and is a mandated closeout target
Last modified **2026-07-02**. `CLAUDE.md:71` makes it a closeout write-target *"if a tracked event resolved."* Since 7/2: formal Hormuz closure (7/11-12), re-arm CONFIRMED (7/16), $85×3 fired (7/21), **Brent >$100 (7/23)**, the −18.1% unwind, the diesel decree. **Many tracked events resolved; the file records none of them.**
**Class:** (a) refresh **or** (d) retire — if TIMELINE is genuinely superseded by CATALYSTS + CHANGELOG, it should be frozen-bannered rather than left to rot as a live closeout target.

### F10 — `domain/REFERENCE_TABLES.md` (boot step 4) is a **March-2026 baseline** including a Hormuz transit section
Header is honest (*"⚠️ VINTAGE: March 2026 baseline reference," stamped 7/21*) — **good practice, flagged for content not hygiene**: its **"Hormuz Transit Volumes"** section describes a pre-closure world (regime mean has gone 89.9 → 9.9 transits/day). Structural constants (capacities, quotas, breakevens) are fine; the transit table is the one section a fresh session could misread as current.
**Class:** (a) — scope-limit or date-stamp the transit section specifically.

### F11 — `scripts/thresholds.py:83` cites **"THESIS v5.1"**; THESIS is **v5.2**
Version-cite only; the threshold content is unaffected and correct.
**Class:** (a) trivial.

### F12 — `STATUS.md:9` (7/30 banner) still asserts the **superseded** gasoline figure
*"the GASOLINE ban that was extended — to **Dec 31 2026**."* The 7/30 decree puts it at **Jan 31 2027**. The 7/31 banner above it explicitly supersedes and labels the correction, and dated banners are historical record by convention — **but a grep for the ban's end-date lands on the stale line first.**
**Class:** (a) low — annotate in place rather than rewrite history.

---

## ✅ CLEAN — seeds checked and CONFIRMED NEGATIVE (verified precisely, not spot-checked)

### F13 — **SEED ① PREMISE IS ITSELF STALE — reporting back.** The spawn packet said *"your 7/28 fighting-shape review noted your boot protocol lacks a general-inbox step; compensate manually this session."* **The step EXISTS and has since 7/28:** `CLAUDE.md:48` **step 6b** (general inbox triage, with the moved-file/ledger-row reconcile), its closeout twin **13a** (`:76-79`), and the amended MAIL rule (`:84`). **There is no gap; no manual compensation was required.** *(I did run it — the general inbox was empty at boot; the PROME packet arrived mid-session and was consumed 1:1 under the same step.)*

### F14 — **SEEDS ② and ④ CLEAN, and I nearly mis-reported both.**
- **Seed ② (frozen-ledger sourcing):** `grep -l` flags `thresholds.py` — **but the hit is line 9, a COMMENT documenting the 7/28 fix** (*"The old header credited `workbook/VX.tsv`, which has been FROZEN since 2026-06-14"*), **not a live read.** No sibling script sources a frozen ledger: `lessons_check`→LESSONS_INDEX · `predictions_due`→PREDICTIONS · `catalyst_countdown`→CATALYSTS · `eia_weekly`→EIA API · `thresholds`→hardcoded-from-THESIS. **CLEAN.**
- **Seed ④ ("2 of 2" residue):** a naive grep hits `STATUS.md` ×4 and `NEXUS_BRIEF.md` ×1 — **every one is inside a sentence RETIRING the claim** (*"the 'STNG veto blocked 2 of 2' claim is RETIRED AS UNVERIFIED"*). The remaining hits at `STATUS.md:21/168/201` are **"wk 2 of 2"** — the unrelated Cushing boundary usage. **No surface asserts the retired tally as live. CLEAN.**
- ⚠️ **Method note, because it nearly went the other way:** my first pass concluded "clean," a second pass raised a false alarm on line-collisions, and only a character-level `grep -o` settled it. **Reporting the method, not just the verdict** — a substring match on a 3,000-character banner line is not evidence of anything (`[[finding_reconcile_match_on_key_not_substring]]`).

### Also checked, no flags
`docket/CATALYSTS.tsv` — **no rows older than 7/24**, so the 1-week prune rule is current; the diesel row is correctly RESOLVED and successors (9/1, 2027-01-31) are registered. · `workbook/{KB,VX,FLOW,GROUP_MAP}.tsv` — all four carry correct FROZEN banners. · `LESSONS_INDEX.tsv` — 21/21 indexed, **zero unresolved contradictions** (first clean run since the checker was built 7/30). · `PREDICTIONS.tsv` — parses, predictions-due scan clean, 7/31 header note present. · All 5 boot scripts run green.

---

## SUGGESTED ORDER (for the disposition round — **not applied**)

1. **F1** — consumer-facing falsehood, another agent's input. Everything else is internal.
2. **F3** — needs a ruling and is the only flag that can silently mis-steer a fresh boot.
3. **F6/F7** — root-script, PROME-owned; F6 is what would have caught F1.
4. **F2, F8, F9, F12, F11, F5, F10** — mechanical.
5. **F4** — threshold move, Will's call.

**No thresholds moved. No edits applied. Nothing UNVERIFIED presented as fact.**

*BRENT · 2026-07-31 11:56 EDT*
