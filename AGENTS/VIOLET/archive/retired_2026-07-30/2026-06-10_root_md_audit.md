# VIOLET Root .md Audit — 2026-06-10 (~11:00 ET, Will ask)

Scope: all 9 root .md files. Ranked by **behavioral impact** (would the agent DO something wrong?), not line count. Freshness baseline: STATUS / SCRATCH / NEXUS_BRIEF / TRADE rewritten 6/9-6/10 and healthy; the rot is concentrated in the three docs nobody owns.

**Root cause up front:** `README.md` and `SIGNAL_INTAKE.md` appear in NO maintenance table — CLAUDE.md's FILES YOU MAINTAIN omits both. Unowned docs rot. Fix the ownership gap, not just the instances.

---

## 🔴 1. SIGNAL_INTAKE.md (last updated 5/3) — action playbook contradicting two falsifications

The worst offender because it's an ACTION playbook (sizing + vehicles + triggers), not reference.

- **a. Unqualified "94% hit rate" with sizing keyed to it.** SKEW Divergence Trigger section: "94% hit rate for ≥15% VIX rise within 60d (15/16, KB-VIO-036)" + "full size 2% account." This is the exact conflated-citation class KB-VIO-079 canonicalized 6/9: rate must carry threshold × tier × unit (STRICT 94% / DIET 92% at ≥+15%; only 56-60% at ≥+50% — and far-OTM strikes price off the LOWER number). The 6/9 sweep fixed thesis/TRADE/MEMORY/Pred#5 but missed this file.
- **b. Term Structure Watch table says inversion = "🔴 Alert — leading indicator."** Falsified in v3.1 (KB-VIO-034: 553 events, 2.2% hit rate — marks PEAKS, exit-timing only, never entry). The OUTBOUND table at the bottom of the SAME FILE was corrected ("Peak marker (v3.1)"); the internal-monitoring table wasn't. Internal self-contradiction.
- **c. Default vehicle "Buy VIX calls 30-60 DTE."** Contradicts the Episode-17 post-mortem vehicle rule now in TRADE.md (fixed-expiry OTM calls die on timing even when the signal is right; match vehicle to channel + timing uncertainty).
- **d. SIGNAL PROCESSING PROTOCOL + outbound table** reflect the HERMES/outbox era (WALTER as SKEW-divergence target, outbox for 🟠 conditions). Current protocol: NEXUS_BRIEF primary, outbox 🔴-acute only, no inbox processing on normal spawns.
- Still good: VVIX/SKEW watch tables, sweet-spot trigger, false-positive patterns, episode database — consistent with MEMORY/thesis.

**Recommendation:** rehab pass (a-d), then either add to CLAUDE.md FILES table with cadence "on thesis bump" or fold the playbook into thesis/TRADE and retire the file. Don't leave it unowned.

## 🟠 2. README.md (last refreshed 5/3) — the front door points at a retired file

- **a. Directory map lists `LAST_COMPLETION.md`** — retired; SCRATCH.md is the handoff. Map omits SCRATCH.md, NEXUS_BRIEF.md, thesis/CHANGELOG.md, CATALYSTS.tsv/COT_VIX.tsv.
- **b. Core Thesis quotes the unqualified "94% (KB-VIO-036)"** — same KB-VIO-079 class as above, sitting at the directory's front door.
- **c. Cross-agent network lists WALTER as a send target** — not in CLAUDE.md's send table; messaging-era residue.
- **Recommendation:** 15-minute refresh + add to maintenance table (cadence: on protocol/thesis change).

## 🟠 3. CLAUDE.md — template residue + internal protocol contradiction *(extends orchestrator item 7b)*

- **a. KEY THRESHOLDS table:** all "Current TBD" since April — never wired, STATUS owns live values. Drop the Current column or point at STATUS.
- **b. CONVERGENCE MATRIX section:** template rows ⚪/TBD/"Never" — STATUS owns the real one; replace with a pointer + the scoring scale. *(Also: 6/9's matrix summed 13/40 vs 17/40 implied by its own emoji scores — scale was never pinned down. Today's STATUS pins the integer scale; CLAUDE.md should state it once.)*
- **c. Boundary rule says "HERMES (the mail carrier agent) will deliver"** — contradicts the MAIL section of the same file (messaging overhauled, HERMES unreliable).
- **d. CROSS-AGENT SIGNALS table** implies outbox files for 🟠 conditions — contradicts write-back step 12 (NEXUS_BRIEF primary, outbox 🔴-acute only).
- **e. RESEARCH PRIORITIES** are the April bootstrap list — #1 regime library, #2 credit-vol lag, #4 crisis analogs: done; #3 term structure: falsified/refined v3.1; #5 options flow: tooled. Replace with pointer to STATUS research queue.
- **f. FILES YOU MAINTAIN:** add README.md + SIGNAL_INTAKE.md (or record the retirement decision).

## 🟡 4. MEMORY.md — subtraction job confirmed + 3 specifics *(extends item 7a)*

- **a. Footer says "Last Updated 2026-06-01" but file was edited 6/9** (principle 6 KB-VIO-079 correction). Footer drift.
- **b. Session notes out of chrono order:** 5/03 → 4/17 → 4/16 → 5/21 → 6/01.
- **c. Trajectory gap:** no session note for the 6/5-6/9 episode (NFP spike, L1 fire resolution, two-leg fade, KB-VIO-074-081 arc) — the biggest episode of the quarter lives only in KB rows + overwritable SCRATCH. One short pointer-note (not a full write-up — subtraction job is the priority) keeps the trajectory readable.
- **d. Duplication-to-pointers** (regime defs / credit-vol synthesis / crisis analogs / SKEW patterns vs thesis) + stale Apr-12 OPEN QUESTIONS FOR WILL (Q1 partially + Q2 + Q3 overtaken: boot.py automation exists, M1:M2 tracking exists, NEXUS_BRIEF replaced outbox automation) — as previously flagged.

## 🟡 5. CALENDAR.md — small residue (file otherwise fresh today)

- **a. DATA REFRESH SCHEDULE "Last Updated" column** all says 6/1 — rows actually refreshed 6/9-6/10 *(item 7c, confirmed)*.
- **b. "VIX options OI ... 2026-04-17 (overdue)"** — wrong twice: it runs in boot.py every boot now.
- **c. Footer says 6/06/6/07** — file edited 6/10 (CPI resolved-section) without footer bump. *(My miss this morning.)*
- **d. VERIFY: Sep FOMC day-count** — FOMC table says "Sep 16-17" (decision = 17th) while CATALYSTS.tsv + expiration table say 9/16 decision "same day" as expiry. One is off by a day; check the Fed calendar before editing (KOYOMI/FASTOW pre-fire-date-verification class).

## 🟢 6. Healthy / no action

- **STATUS.md / SCRATCH.md / NEXUS_BRIEF.md** — rewritten today; STATUS ~120 lines (under cap); EOD re-stamp already owed and tracked.
- **TRADE.md** — rehabbed 6/9; one nit: when the fade gate re-adjudicates at EOD, add a one-line adjudication log under the LIVE DECISION FRAMEWORK (6/10 AM: gate #1 FAILED, deferred — KB-VIO-081) so the proposal→decision loop closes in the originating file.

---

## Suggested execution order (if approved)

1. SIGNAL_INTAKE.md rehab (a-d) — highest behavioral risk, ~30 min.
2. README.md refresh — ~15 min.
3. CLAUDE.md residue pass (a-f) — ~30 min; protocol file, so change conservatively.
4. CALENDAR small fixes + Sep FOMC verify — ~10 min.
5. MEMORY.md subtraction job — biggest job, already queued as its own housekeeping session (item 7a); fold a/b/c into it.

Items 1-4 fit one sitting; item 5 stays a separate session per the 6/9 orchestrator plan. All consistent with the existing SCRATCH item-7 housekeeping list — this audit extends it with SIGNAL_INTAKE/README (which item 7 missed entirely, because they're unowned — see root cause).
