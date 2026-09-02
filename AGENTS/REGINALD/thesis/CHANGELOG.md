# REGINALD CHANGELOG

**Reverse chronological — newest first.** Each entry documents what changed, why, and old view vs new view. This is the audit trail, never the current state.

⛔ **BOTH PARENT DOCUMENTS ARE RETIRED** — `THESIS.md` (R1, 2026-08-13) and `TIMELINE.md` (R2, 2026-08-20). **`STATUS.md` is thesis-canonical; `CALENDAR.md` owns forward dates.** This file is now the ONLY live file in `thesis/`; the other two paths are pointer stubs — **never edit a stub to satisfy this file's rule.**

**What triggers an entry now:** a **THESIS-LEVEL claim moving on `STATUS.md`** — not an edit to a retired document. A price crossing a registered line is a *state* change and earns an entry only when the underlying claim moves with it (see the 2026-09-01 entry, which logs a fire and records explicitly that the mechanism claim did NOT move).

⛔ **Versioning is RETIRED with the documents.** THESIS's `vX.Y` line ended at v1.4; TIMELINE was never numerically versioned. **Entries are DATED, not versioned.** *(If a v2.0 successor is ever written from STATUS's narrowed claims, versioning resumes with it — and do NOT resurrect an eight-channel document.)*

---

## ✅ POST-RETIREMENT ERA — `STATUS.md` IS THESIS-CANONICAL (entries below are STATUS thesis-STATE changes, not document changes)

> ⚠️ **STRUCTURAL FIX 2026-09-02, and it was a real navigation defect:** this file declares *"reverse chronological"* at the top, and the **newest entry (2026-09-01) was sitting at the very BOTTOM — below the file's footer and below a banner reading `THIS CHANGELOG IS CLOSED FOR THESIS-DOCUMENT ENTRIES`.** A reader travelling top-down hit *CLOSED*, read it as the end of the file, and never reached the live entries. **The banner is scoped to thesis-DOCUMENT entries and these are STATUS thesis-STATE entries — a different class that the container silently suppressed.** `[[finding_live_claim_in_a_closed_container_is_invisible]]` Post-retirement entries now sit at the TOP where the stated ordering says they belong.

## 2026-09-01 — `REG-T-02` FIRED (WAL $77.26 close) — thesis-STATE change on `STATUS.md#wal-v1v3-thesis`; the mechanism claim did NOT move

**Authority:** owner grade, REGINALD, at the registered instrument (`registry/NOTES.md §REG-T-02` ruling 2026-09-01). Logged here because the trigger's `threshold_thesis_ref` is the WAL V1/V3 leg of the thesis-canonical `STATUS.md`, and a registered-trigger state flip is a thesis-state change under the RE-SCOPED rule (2026-08-20).

**Old view → new view:**

| Until 9/1 | From 9/1 |
|---|---|
| `REG-T-02` **UN-FIRED** since the 6/30 exit; seven closes above the line 8/21→8/31 (79.67 → 78.13), buffer quoted per close | **FIRED** on the 9/1 close ($77.26, 0.95% below); **cycle 2 open**; exit `≥81.90 ×3` LIVE (0-of-3). Sub-78 re-entries suppressed. |
| "WAL <$78 = hidden-CRE thesis accelerating" (KEY THRESHOLDS implication, unchanged wording since spring) | **The LEVEL fired; the MECHANISM did not.** V1 (MI3) disconfirmed 8/7 (<25% ×12q); V3 (NDFI) 11-for-11 no reserve build Q2; 9/1 was a sector day (WAL −1.11% < KRE −1.28%, cohort median, ρ(PC-NDFI, move) +0.253). The `V1V3-ACCELERATE` routing is executed as a **letter obligation**, with the attribution attached so it cannot be re-read as evidence. |

**Not changed:** severity CONCENTRATED-not-tier-wide (matrix v2.0), no threshold, no prediction confidence, no matrix score. **What is now live that was not:** the exit condition (graded every close) and a Will decision on the Sep-18 67.5/70P pair (routed).

### Also 2026-09-01 — the last open row of the retired `TIMELINE.md` closes: First Brands auction recovery → **RESOLVED-BY-SUPERSESSION (2026-08-24, Ch.7 conversion ordered)**
The 8/20 R2 retirement left one branch point open (Mar 31 First Brands auction recovery, 40% line). BROCK 8/28: the recovery was **never established as an auction print**, but the question it proxied — permanent charge-off vs temporary mark — is answered at the docket: plan confirmation **DENIED 2026-08-24** (Dkt 3710, Lopez), all debtors ordered to **Chapter 7** (Dkt 3722); marks 13-16¢ senior / ~0.4¢ 2L [Feb-2026] ⇒ **below 40%, and the reorganisation path that was the only route above the admin-expense floor is gone.** Resolves in the pre-registered direction (permanent charge-offs). ⚠️ Guard carried: the **$237M / 15-BDC figure is PAR, not carrying value** — remaining markdown capacity ~$31-38M sector-wide (BROCK, upper bound, estimate). Not edited into the archived TIMELINE (history stays byte-intact); recorded here and in ROADMAP §Recently Resolved.

---

## 2026-08-20 — ⛔ RETIREMENT **R2**: `TIMELINE.md` ARCHIVED (not rewritten). Both thesis docs are now retired; `STATUS.md` + `CALENDAR.md` carry the load.

**Authority:** Will, in-session — *"lets go with your recommendations. I do not need to rule on it I don't think."* Reviewed and proposed by REGINALD the same session. Follows **R1** (`THESIS.md`, Will-ruled 2026-08-13).

**What changed:** `thesis/TIMELINE.md` → `archive/thesis_TIMELINE_v1.4_2026-04-02.md`, replaced by a pointer stub. **No rewrite. No successor.**

**Old view vs new view:**
- **OLD:** a week-by-week forward catalyst calendar with branch points, owned by `thesis/`, carrying its own POSITION CALENDAR and its own "our view" per event. Last content update **2026-04-02**.
- **NEW:** forward dates are owned solely by **`CALENDAR.md`** (live, maintained, boot-read at step 3); thesis state by **`STATUS.md`** (canonical since R1); per-event bull/bear forks by **frozen grading frames** in `reports/`. **The `thesis/` folder now holds only `CHANGELOG.md` (this file) and two pointer stubs.**

**Why retired rather than rewritten — four reasons, in order of weight:**
1. **A rewrite creates a SECOND forward calendar.** `CALENDAR.md` already owns forward dates per the Doc Ownership table. Two forward calendars = two sources of truth for dates = the exact drift vector behind the 6/19 desync incident.
2. **The skeleton WAS the retired thesis.** Organised entirely around the eight-channel "detonation window" retired at R1 for arguing the opposite of the live view. A faithful rewrite needs new structure ⇒ it is a new document, not a rewrite.
3. **It was an ACTIVE PHANTOM SOURCE.** Its POSITION CALENDAR re-listed strikes/expiries — **OWL $9.5P, SSB $90P, IWM $250P, WAL $85P** — and **SSB $90P + IWM $250P are the two named cases in `LESSONS.md`'s phantom entry.** The Doc Ownership rule (POSITIONS.md canonical; others POINT, never re-list) had never been extended to this file. Retiring closes the hole.
4. **Two cycles overtaken:** 11 branch points still read `PENDING` months after resolving; the Q1-earnings-wave framing was superseded by the 6/8 cohort resolution (Hypothesis A, benign) and the 8/10 FL watch-card close (4-of-4 REVERT ⇒ concentration, not tier).

**★ HARVESTED BEFORE ARCHIVING — retirement without harvest loses real content, so three things came out:**

**H1 — the AOCI / capital-rewrite thread was LIVE and had NO live home, and its framing was WRONG on two axes.** Now a `CALENDAR.md` row (H2-26/Q1-27) + a re-pointed `ROADMAP.md` thread.
- ✅ **Kept and re-sourced:** mandatory AOCI inclusion in CET1 for **Cat III/IV** ($100B-$700B), ending the opt-out. **$49.5B aggregate across 21 firms** — Risk.net / Risk Quantum, **SECONDARY, flagged as such** (TIMELINE cited it naked).
- 🔴 **CORRECTED — DIRECTION:** TIMELINE called it *"the slow-burning bomb… a SEPARATE capital drain on top of credit losses"* and built a **compound-capital-drain** thesis on it (CRE charge-offs + AOCI hitting the same bank from two sides, *"the market isn't modeling this compound effect"*). **That is one-sided.** The AOCI leg is real but the package **nets to a capital REDUCTION** for Cat III/IV — ~0% CET1 change at holdcos, **−4.7% at depository subsidiaries** — because other changes offset it.
- 🔴 **CORRECTED — TIMING:** **five-year phase-in running to 2032** (100% excluded in year 1 → 0% by 2032). A drip, not a 2026-27 event. The compound thesis required it to land *alongside* CRE recognition; on this schedule it does not.
- ⚠️ **Status 2026-08-20: still PROPOSALS.** Comment closed 6/18/26, no final rule. **The bear read revives only if the final strips the offsets and leaves the AOCI leg standing** — that is now the registered watch condition.
- ★ **Side finding:** `domain/research/capital-rewrite-2026/` (34-ref source memo + KBRA compendium, dated 3/26-27) was **referenced by ZERO live surfaces** and its INDEX advertised **two files that do not exist**. Both fixed. ⚠️ **And a RULE GAP surfaced: my research-retirement rule (>60d + not boot-read + not referenced → archive) matched this folder on all three conditions and would have ARCHIVED A LIVE THREAD.** The rule has no "is the underlying event still pending?" test. Flagged in ROADMAP, not silently applied.

**H2 — the Branch Point Summary format, kept as LINEAGE not as a table.** `Date | Event | Bull fork | Bear fork | Status`, pre-registered before the event, is the **direct ancestor of the frozen grading frames** now used well (EGBN Q2, ZION cross-read scaffold, FL small-tier watch-card). **Deliberately NOT rebuilt:** per-event frames that are frozen and graded verbatim are strictly better than one standing table that rots between events. **The practice outlived the document.**

**H3 — one branch point never resolved and was NOT allowed to die with the file.** *Mar 31 — First Brands auction | low recovery (<40%) = permanent losses | ❓ RESULT UNKNOWN* — open ~5 months. Packeted to **BROCK** (owner) 8/20 asking whether the recovery rate ever landed; *"never publicly established"* is an accepted answer, and the row closes as `UNRESOLVED-PERMANENTLY` if so.

**⚠️ One deliberate REVERT, recorded so a future reader does not read it as rot:** earlier the same session I patched TIMELINE's FHLB line from `~$480B` to the live `$810.7B`. **That patch was reverted before archiving.** A fresh number inside a dead document is worse than a stale one — it *certifies* the page (`finding_header_edit_is_the_edit_most_mistaken_for_maintenance`). The archived copy is now a faithful 2026-04-02 artifact; the live FHLB figure lives in `VX-REG-7.01` + `STATUS.md`.

**No version bump** — TIMELINE was never numerically versioned (see the convention note at the top of this file); the retirement is dated, not versioned.

## ⛔ 2026-08-13 — v1.4 RETIRED. THIS CHANGELOG IS CLOSED FOR THESIS-DOCUMENT ENTRIES.

**Change:** `THESIS.md` (v1.4, last substantive update 2026-04-16) `git mv`'d to `archive/thesis_THESIS_v1.4_2026-04-16.md`; a **pointer stub** left at the original path so inbound links do not dangle. **`STATUS.md` is now CANONICAL for thesis state.**
**Authority:** Will-ruled in-session 2026-08-13, on REGINALD's own retirement proposal R1, option (ii) — logged here because this file's own rule says *any* change to `THESIS.md` requires a CHANGELOG entry, and retiring it is the largest such change there will ever be.

**Old view → new view:**

| v1.4 asserted (2026-04-16) | The live view at retirement |
|---|---|
| *"Eight independent channels, six at 🔴+, Status 🔴🔴🔴 CRITICAL, conviction HIGH"* | **🟠 ELEVATED**, and narrowed to **concentration at OZK/EGBN, NOT tier-wide** — five independent confirmations (cohort NCO decomp 6/8 → Hyp A · CRE-DQ-by-tier drill 6/20 · EGBN Q2 de-risking 7/25 · FL small-tier watch-card 4-of-4 REVERT 8/10 · benign large-cap Q2 cohort) |
| Channel 2 "Hidden CRE" 🔴, per-bank ratio table | **Measured EMPTY as a cross-bank screen** (8/13 cohort re-run, 168 bank-quarters at the FFIEC primary). The legacy `>20%` flag is **RETIRED** — its basis is not cross-bank comparable **and** `RCON2746` is a step-prone line (17/154 = 11.0% of bank-quarters), so it is unreliable across time too. The **mechanism** (bucket migration) survives; the ratio does not. |
| Credit transmission live | **`BANK-ABSENT`, conf ~0.8** (7/30 attribution, unretracted) — HY sits downstream of bank credit in this chain |
| WAL / OZK deep coverage in-thesis | **Peer agents since 7/25 and 7/22** — `../WAL/`, `../OZK/` own their own theses |

**Why RETIRED and not REFRESHED:** it had carried *"full refresh scheduled post-Jul-21"* since 2026-07-10 and lost to live work every session — but the deciding reason is **disagreement, not staleness.** A stale document is a maintenance cost; **a stale document that argues the opposite of the live view is a liability**, and a banner does not stop a reader lifting the channel table. **The eight-channel frame earned its retirement by being tested and narrowed, which is a success.**

⚠️ **Do not resurrect an eight-channel document.** A successor, if ever wanted, is a **v2.0** written from `STATUS.md`'s narrowed claims — a 2–3 channel document, not a refresh of this one.
**This file stays as history and is not deleted.** ⚠️ **SUPERSEDED 2026-08-20: `TIMELINE.md` is NO LONGER LIVE — retired at R2.** *(Original text follows: TIMELINE.md remains live — ⚠️ carries v1.4-vintage figures — read against STATUS)*, so a TIMELINE change still earns an entry here.

---

*~~Thesis → `THESIS.md`~~ → **RETIRED 2026-08-13. Thesis state → `../STATUS.md` (canonical). Archived original → `../archive/thesis_THESIS_v1.4_2026-04-16.md` (history only).***
*Timeline → ⛔ RETIRED 2026-08-20 (R2). Forward dates → `CALENDAR.md`; archived original → `archive/thesis_TIMELINE_v1.4_2026-04-02.md`.*

---

## ⛔ DOCUMENT-ERA ENTRIES (2026-03-31 → 2026-07-17) — ROTATED 2026-09-02

*21,915 B, verbatim + contiguous, crc32 `7a6dbe1c` → `archive/thesis_CHANGELOG_document-era_2026-09-02.md`.* Every entry from when `THESIS.md`/`TIMELINE.md` were LIVE: v1.0 baseline → v1.4, the WAL bank-thesis v1.0→v2.2 entries, the TIMELINE branch-point table, the pre-changelog summary. **Both parents are retired and neither returns.** Read the archive for how the thesis got here, never for what it claims now.

**Re-check this file's size at any append, or on 2026-10-02, whichever is first.**

---
