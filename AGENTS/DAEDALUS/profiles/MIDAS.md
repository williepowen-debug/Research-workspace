# Agent Profile — MIDAS

**Built by:** DAEDALUS · **Date:** 2026-09-05 (**FIRST BUILD** — the desk was built 2026-07-11 and ran 8 weeks without a comprehension layer)
**Method:** solo full-tree read + guards RUN (`boot.py` rc=1, `metals_watch.py`/COT grader presence, ledger row counts, CLAUDE.md rot re-measured line by line)
**Sources read:** `CLAUDE.md` (217 ln) · `STATUS.md` (105) · `THESIS.md` · `TRADE.md` · `LESSONS.md` · `SCRATCH.md` · `OPEN_ITEMS.md` · `NEXUS_BRIEF.md` · `workbook/` (5 TSV + a Kernel companion JSON) · the six top-level scripts · `registry/` · `kernel/` · `analysis/` · `reports/`
**Staleness:** refresh at the next COT-grade cycle or **>21d** → checkpoint **2026-09-26**

> **Receipt update 2026-09-08.** Before this update: `archive/2026-09-08_INBOX_PROFILE_BEFORE_IMAGES.json` (verbatim bodies + SHA-256). Evidence and dispositions: `runs/2026-09-08_INBOX_DISPOSITIONS.md`.

---

## 1. Identity
**Metals as TWO distinct macro tells** — Market class, ACTIVE, L4 (H), graded 2026-09-08. *Monetary* (gold/silver: debasement, real-rates, safe-haven) and *industrial* (copper/PGM: growth, China demand, supply). Built by DAEDALUS 2026-07-11 to spec (`builds/MIDAS_SPEC.md`). Feeds **BOND** (gold ↔ real rates), **ZHAO** (copper ↔ China), **LIQUID** (safe-haven flow), **HAWK** (PGM supply geopol), **HENRY** (growth/inflation tells).

**⭐ The #1 guard is a scope guard, and it is the reason this desk exists rather than DARWIN:** *channels, not commodity-watching.* Each channel is a standing causal line (`event → mechanism → repricing`); **an empty channel is a gap to close, not idle background**; "track commodities broadly" is the named failure mode. Any upgrade proposal that widens coverage is arguing against the charter's founding constraint.

## 2. File anatomy
| Cluster | Files | Notes |
|---|---|---|
| Governing | `CLAUDE.md` 217 ln | channels-first guard · boot sequence · channel definitions |
| Live state ⭐ | `STATUS.md` 105 ln | **the most label-disciplined live surface on the fleet** — see §4.1 |
| Thesis / routing | `THESIS.md` · `TRADE.md` | TRADE has been **re-based four times**, the fourth being *"the FIRST band ever COMPUTED rather than derived"* |
| Record | `workbook/` — `KB.tsv` 107 · `PREDICTIONS.tsv` 8 · `VX.tsv` 5 · `FLOW.tsv` 4 · `SCHEMA.tsv` | small VX/FLOW **by design** (few channels, kept live) |
| Instruments | `boot.py` · `metals_watch.py` · `cot_gold.py` · `grade_cot3.py` · `grade_midas07.py` · `settle_check.py` | ⚠️ **scripts live at the TOP LEVEL**, not in `scripts/` — unusual; don't "tidy" them into a subdir, the paths are cited |
| Governance | `registry/corrections_receipts.tsv` · `kernel/staged_submissions/` | Gate-C shadow path (carve-out ④) |
| Learning | `LESSONS.md` · `OPEN_ITEMS.md` · `SCRATCH.md` · `analysis/` · `reports/` | |

## 3. Per-dimension
| Dimension | Where | Form |
|---|---|---|
| Thesis | `THESIS.md` + STATUS channel reads | two-tell split (monetary M-*/industrial I-*) |
| Convergence | `VX.tsv` (5) + STATUS composite | **composite scored /20** (e.g. M1 3→4, composite 7/20→8/20) |
| Exit / kill | THESIS kill-conditions, numbered (`kill-cond #3`) with sustain bars ("full kill needs 3+wk sustain") | |
| Predictions ⭐ | `workbook/PREDICTIONS.tsv` — id · made · channel · **resolve_date · conf_tier · if_falsified · criteria · resolution** | the `if_falsified` column is a **pre-committed consequence**, not a note — §4.2 |
| Routing | STATUS flags + `NEXUS_BRIEF` + outbox | BOND adopted a MIDAS carve-out **verbatim** 9/1 |

### §3b. Invalidation-surface inventory
| Surface | Kills / flips | Stamp | Fired-state |
|---|---|---|---|
| `THESIS.md` kill-conditions | the monetary/industrial channel reads | in-content, numbered + sustain bar | "kill-cond #3, fired 8/7" |
| `PREDICTIONS.tsv` `if_falsified` | the specific channel + the composite score | `resolve_date` per row | `status` + `resolution` |
| `STATUS.md` ⛔ superseded blocks | prior published marks | ⛔ banner + dated supersede note | struck in place, kept visible |
| `TRADE.md` re-base banners | the routed band figure | "RE-BASED 2026-08-27" ×4 | each re-base names what it corrected |

## 4. Deviations — two that are better than standard

**4.1 — STATUS labels every mark with its own trustworthiness, and strikes its own claims in place.** Live examples: *"`GC=F` — **thin dying contract, vol 360, O=H bar; DO NOT USE**"* · *"⛔ THE 8/31 GC=F ROLL CLAIM ON THIS PAGE IS SUPERSEDED (KB-099)"* · *"⛔ THE VOLUME DISCRIMINATOR WAS UNAVAILABLE ON THE 9/1 ROW"* (all 7 tickers returned 8/31's volume duplicated into 9/1) · *"verified independently at the primary 23:51Z, **not taken from BOND's packet**"*. The header opens with a **⛔ CITE** instruction telling readers which construction to quote. **A desk that publishes the reliability of each number beside the number is doing the expensive half of the job.**

**4.2 — `if_falsified` is a pre-committed consequence and MIDAS-08 is the exemplar.** It states, before the event: *"IF (c) FIRES: my published line … must be re-read **IN PUBLIC** as too strong … Write it plainly on STATUS and route the correction to BOND, which adopted that carve-out verbatim 9/1. **A falsifier that fails to fire is information about MY FALSIFIER, not a vindication of my read.**"* And the reverse: *"IF (a) FIRES: it does NOT retroactively validate MIDAS-06, does NOT re-open MIDAS-07…"* — both directions pre-bounded. **This is the strongest single prediction row I have read on the fleet** and it should be the fleet exemplar for `if_falsified`.

**Legitimate small ledgers.** `VX` 5 rows, `FLOW` 4 — a *feature* of channels-first, not thinness. Do not grade MIDAS against row counts.

## 5. Findings

**F-1 — CLOSED-VERIFIED 2026-09-08.** MIDAS-08 is terminal INDETERMINATE, owner-graded 2026-09-05. Branch (c), which would require the public correction to BOND, did not fire. Both directions were pre-bounded; that is not a promise that every outcome creates a correction obligation.

**🟢 F-2 — RESOLVED 2026-09-05 by MIDAS, and my original framing was TOO BROAD (Codex 2026-09-05, verified at `AGENTS/MIDAS/boot.py`).** *Original:* "three COT graders shipped and `boot.py` never calls them — detection built, invocation missing; fourth instance of a fleet pattern." MIDAS's correct answer was **narrower**: it wired ONLY `cot_gold.py` (a PULLER on a standing weekly cadence whose live STATUS figure was rotting — 56.86% [8/25] while the 9/1 vintage was public 9/4), and **deliberately** left `grade_cot3.py`/`settle_check.py` on-demand, documenting in `boot.py` *"so the next reader does not fix the other three."* **They grade CLOSED questions; running them on a boot cadence would reapply frozen grading logic to new data — a NEW defect.** ⚠️ **The discriminator I missed:** "invocation missing" is a defect ONLY for a detector measuring a MOVING quantity on a standing cadence (a puller); a grader for a closed question is CORRECTLY on-demand. My note treated all four uniformly. Closes F-2 (cot_gold.py wired); refines the invocation-missing class → 9/14 ladder-integrity input (`runs/2026-09-05_CODEX_REVIEW_FINDINGS.md`).

**F-3 / F-4 — CLOSED-VERIFIED 2026-09-08.** No `(when built)` text remains in CLAUDE.md; STATUS labels its local scale `Instrument coverage: tier 2`. The former L2 label survives only inside an explicit correction.

**New open owner item:** `OPEN_ITEMS.md` item 24 records a missing contract-identity guard, with an interim explicit-contract rule. This remains open; closing the four prior findings does not close it.

**✅ Verified clean:** `boot.py` runs and its rc contract is honest (1 = prediction due) · the four self-found defects of the 9/2 session are recorded with the peers who caught them (*"three peers corrected me and all three were right"*) · `registry/corrections_receipts.tsv` present · Kernel submission path is the canonical immutable form.

## 6. DO NOT TOUCH
1. **Channels-first.** Never propose broadening coverage; "track commodities broadly" is the named DARWIN failure this desk was chartered against.
2. **Scripts live at the top level, not `scripts/`** — paths are cited in CLAUDE.md and STATUS. Don't tidy.
3. **The ⛔ superseded blocks in STATUS** are corrections kept visible on purpose. Never delete a struck claim; the strike is the record.
4. **`GC=F` vs `GCZ26`** — the front/dying-contract distinction is load-bearing and STATUS says which to cite. Never average or silently substitute them.
5. **`if_falsified` pre-commitments are binding text**, especially MIDAS-08's public-re-read clause. Do not soften one after the outcome.
6. **The band figure has been re-based four times, each naming what it corrected** — cite the current construction *by name* (univariate 87.7–91.1% vs currency-stripped 90–93%), never a bare percentage.

## 7. Grade and remaining scope
- L4 PASS with the established declared-flat adaptation: TRADE.md states zero capital by design and requires a registered trigger, T+1 confirmation on both bases and a signal with falsifier to TERRY before unfreezing. The concrete declaration closes the prior open applicability question.
- Cross-desk consumption is real: BOND/NEXUS_BRIEF cites MIDAS's gold evidence and source-label correction; BOND workbook holds the adopted caveat. No new position or trade proposal follows from this grade.
- L5 not adjudicated; contract-identity guard stays open. Profile checkpoint remains 2026-09-26.
