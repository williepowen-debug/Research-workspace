# WAL — retirement sweep record, 2026-08-23 (session #4)

**Authority:** Will, in-session 2026-08-21, verbatim *"Rule the WAL parked ×2 off your recs."* Ruling of record → `PROME/proposals/2026-08-21_wal-parked-x2-RULED-sweep-approved-rider-unfiled.md`; delivered as `inbox/processed/2026-08-21_from-PROME_parked-x2-RULED-sweep-approved-under-amended-rule-rider-needs-text.md`.

**Rule applied (root `CLAUDE.md` § Data Hygiene, as amended 2026-08-21, root batch `326181484`):** a file that is **>60 days old AND not boot-read AND not referenced by a live doc** → `git mv` to `archive/`. Two amendment clauses were load-bearing here:
- ① **pending-event carve-out** — a file that is the registered artifact of a PENDING dated event is not retirement-eligible however old.
- ② **index-refs don't count** — a reference from an index/inventory/nav surface does not satisfy "referenced by a live doc." *(This clause is what makes the sweep possible at all: all four candidates are listed in `INDEX.md`'s deep-dive line, which under the pre-amendment letter made every indexed file immortal.)*

⚠️ **PROME's rider observed: the rule was RUN FILE-BY-FILE, not applied to the list.** The four were candidates, not a pre-approved batch — and one of them failed.

## Dispositions — 3 archived, 1 HELD

| File | >60d? | Boot-read? | Referenced by a **live** doc? | Pending-event artifact? | Disposition |
|---|---|---|---|---|---|
| `TECHNICALS.md` | ✅ Feb/Mar-2026 content (~150d) | ❌ not in the boot sequence | ❌ — `INDEX.md:83` is an **index-ref** (clause ②); `AUDIT_MAR25.md` is itself a March record, not a live doc; `MARKET/STATUS.md` is a co-archived fossil | ❌ | 🗄️ **ARCHIVED** → `archive/TECHNICALS.md` |
| `FORGE_STATUS.md` | ✅ Feb/Mar-2026 (~150d) | ❌ | ❌ — `INDEX.md:83` (index-ref) + `AUDIT_MAR25.md:23` (March record) only | ❌ | 🗄️ **ARCHIVED** → `archive/FORGE_STATUS.md` |
| `MARKET/STATUS.md` | ✅ **Last Updated 2026-03-25** (~151d); carries `Price: ~$68` | ❌ | ❌ — **zero references found anywhere** | ❌ | 🗄️ **ARCHIVED** → `archive/MARKET/STATUS.md` |
| `EARNINGS_PREP.md` | ✅ Feb/Mar-2026 | ❌ | ✅ **YES — and this is the disqualifier** | ❌ | ⛔ **HELD — FAILS THE RULE. Stays in place.** |

### Why `EARNINGS_PREP.md` stays — the reason, not a preference

**It is referenced by two live docs, and one of them is the boot card:**
- **`CLAUDE.md` § DOC OWNERSHIP** — *"`Q2_GRADING_FRAME` / `PREPRINT_RECON` / `EARNINGS_PREP` | 🧊 FROZEN pre-registration + calibration records. Path fixes only, content NEVER."* — plus its § FILES table. `CLAUDE.md` is the **live protocol doc every spawn reads first**; a reader genuinely travels this link.
- **`THESIS.md:413`** — *"`EARNINGS_PREP.md` | Pre-print framework (now historic)"* — a live analytical doc.
- Third, mechanical: the path is **hard-coded in `scripts/derived_drift_check.py` `SKIP_FILES`** (boot step 4c). Archiving it silently un-skips the file and changes the check's baseline — a moved file breaking a live instrument, which is precisely the failure clause ① exists to prevent in the dated-event case.

**Under the amended letter this file does not qualify, so it was not swept.** PROME's rider explicitly allowed holding it; the hold here is on the rule's own arithmetic, not on the rider.

★ **But holding it surfaced a real defect, which is filed as its own rider → `EARNINGS_PREP_BANNER_RIDER_2026-08-23.md`.** The file carries **two mutually inconsistent classifications**: its own banner calls it a *STALE-VINTAGE fossil, do NOT cite as current*, while `CLAUDE.md` calls it a **🧊 FROZEN calibration record whose content must NEVER be edited**. Those are different dispositions with opposite handling rules, and the file has been sitting under both.

## Mechanics performed (PROME's riders, each one)

- ✅ **`git mv`**, not `bash mv` — verified with `git status` immediately after the move (all three reported `R`, so no dangling-deletion residue and no gitignore re-scoping: `finding_git_mv_rescopes_gitignore_rules`).
- ✅ **Banners travelled** — each archived file keeps its original STALE-VINTAGE banner *and* gains a dated ARCHIVED banner naming the rule and pointing here.
- ✅ **Relative pointers repaired in the same edit** — the archived banners' `STATUS.md`/`POSITIONS.md`/`THESIS.md` links were depth-corrected (`../`, and `../../` for the `MARKET/` file), and `archive/MARKET/STATUS.md`'s *"See `TECHNICALS.md` (parent dir)"* now points at its co-archived sibling. **An archived file with broken links is a worse artifact than one left in place.**
- ✅ **Pointer-map footer updated** — `INDEX.md` deep-dive line re-pathed.
- ✅ **`derived_drift_check.py` re-run + counted after** — see the closeout commit for the delta.

## What was NOT swept, deliberately

- **`LEADERSHIP.md`** — bannered STALE-VINTAGE (2026-03-31) and superficially a fifth candidate, but **`THESIS.md:375` travels it for substance** (*"Detail unchanged → `LEADERSHIP.md`"*). Live-doc reference ⇒ fails the rule ⇒ stays.
- **`Q2_GRADING_FRAME_2026-07-21.md` / `PREPRINT_RECON_2026-07-17.md`** — 🧊 frozen calibration records, <60d, and the desk's reference discipline. Never in scope.
- **`AUDIT_MAR25.md`, `EXTERNAL_PROMPTS.md`, `PRIOR_RESEARCH_EXTRACTS.md`, `V21_RESPONSE_TO_RED_CHG_025.md`, `INVESTOR_DAY_*`, `Q1_2026_ANALYSIS.md`, `TECHNICALS_20260401.md`** — old, and several would likely qualify, but **they were not in the ruled scope.** The ruling covered the four bannered fossils. Extending a sweep past its authorization because the files "look similar" is how a ruled action becomes an unruled one. **Flagged to PROME as a possible next-window candidate set; not touched.**

---

*Sweep executed by WAL session #4, 2026-08-23, under PROME orchestration. Zero content edited in any archived file beyond the banner and its own broken pointers.*
