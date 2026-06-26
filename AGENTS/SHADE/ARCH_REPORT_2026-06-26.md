# SHADE Architecture Self-Report
**Date:** 2026-06-26 | **Author:** SHADE | **For:** Prome fleet-wide compare/contrast

---

## 1. Folder Map

| Dir | Purpose | Assessment |
|---|---|---|
| `CLAUDE.md` | Identity, domain, kill-paths, spawn/closeout protocol | **Load-bearing** — boot anchor |
| `STATUS.md` | Live insurer-wrapper dashboard, numbered §-sections | **Load-bearing** — canonical output |
| `SCRATCH.md` | Ephemeral session handoff | **Load-bearing** — boot input |
| `MEMORY.md` | Durable SHADE-specific lessons | Healthy; ~40 lines, not bloated |
| `MAINTENANCE.md` | Structural-change log | Thin — rarely updated; 1 entry |
| `LAST_COMPLETION.md` | Legacy closeout (superseded by SCRATCH) | **Dormant** — should be archived |
| `board_log.tsv` | WALTER signal consumption ledger | Healthy; 2 rows so far |
| `research/` | Deep dives, NPORT crawls, boot sweeps, triage docs | **Heavy / rich** — good provenance but 3 STATUS-rebuild artifacts (STATUS_DRAFT, STATUS_REFRESH_PHASE1/3) are now stale scaffolding; `tmp_aaia_extract/` is session-temp not flagged for cleanup |
| `domain/sources/` | 8 numbered KB docs (PE nexus → Egan-Jones) | **Thin usage** — built Mar'26, not actively cited in session work; possible staleness risk if events have passed |
| `sources/athene_statutory_2026-06-15/` | Raw statutory text extracts (AANY, ALIRT, ALRE) | **Rich but frozen** — 12K+ lines of primary filings; not auto-cited; provenance chain exists via MANIFEST.md but requires manual lookup |
| `inbox/` | Signals: WALTER sublane + top-level legacy | **Mixed** — 5 unprocessed signals in top-level inbox (Apr–May 2026 vintage); WALTER sublane correctly structured |
| `inbox/WALTER/` | WALTER delivery lane; `processed/` subfolder | 5 unprocessed WALTER signals waiting; only 1 processed so far |
| `outbox/delivered/` | Outgoing signals archive | Thin; 1 item (REFRESH_MAR26) — mostly outgoing signals written directly to other agents' inboxes |
| `archive/` | Retired STATUS snapshot | 1 file; appropriate |

---

## 2. Canonical Doc Set

| File | Role | Boot-read? |
|---|---|---|
| `CLAUDE.md` | Identity, kill-paths, key ratios, spawn/closeout protocol | ✅ Yes |
| `STATUS.md` | Live dashboard; 10 numbered §-sections; single source of truth for all insurer-wrapper metrics | ✅ Yes |
| `SCRATCH.md` | Session handoff: changes-since, what-I-did, next-session priorities, open threads, mail state | ✅ Yes |
| `MEMORY.md` | Durable domain lessons; tier between SCRATCH and auto-memory | ✅ Yes |
| `board_log.tsv` | WALTER signal ledger — boot-scan for unprocessed rows | ✅ Yes (per CLAUDE.md §4a) |

No owner→mirror relationships currently. NEXUS_BRIEF.md is specified in CLAUDE.md but not yet built — it would become a mirror-out to NEXUS/PROME.

---

## 3. Knowledge/Data Layer

**STATUS §-section model (10 numbered sections):** §0 = boot-delta with verified threshold table; §1 = top-line read; §2 = domain evidence by sub-topic (Athene defense, AMAPS, NAIC/regulatory, FABN ladder, Egan-Jones, systemic commentary); §3 = signal dashboard (tabular, per-vector status + owner); §4 = transmission-stage map; §5 = watchlist; §6 = regulatory/funding calendar; §7 = cross-agent dependencies; §8 = active questions; §9 = historical notes/retired rails; §10 = next actions with pre-registered lanes. Enables fast boot scan (§0 + §3 + §10) without re-reading the full narrative.

**Trigger-gated dig lane:** STATUS §10 item 6 pre-registers the double-jeopardy entity+fund mapping as an ordered 4-pull sequence with explicit trigger condition (wrapper-decoupling fires OR FABN >250bp/RBC breach/enforcement escalation). Not calendar-driven.

**Default-index series:** Proskauer 2.73% (SHADE-canonical for insurer-portfolio context); Moody's $807B/20% (SHADE-canonical insurer illiquidity quantum). BROCK owns KBRA/Fitch/CDLI series; SHADE references, doesn't duplicate.

**`board_log.tsv`:** v0.2 header (timestamp_read / signal_id / disposition / source / notes). Disposition vocabulary: acted / noted / deferred / info-only / skipped.

**`domain/sources/`:** 8 numbered KB docs built Mar'26 — structured as a reference library (landscape → forensic manual → specific kill-paths). Not actively cited in recent sessions; staleness risk if events have overtaken them.

**`sources/athene_statutory_2026-06-15/`:** Primary filing text extracts with MANIFEST.md provenance. Rich (~12K lines) but frozen at 6/15; manual lookup only.

---

## 4. Processes

**Boot:** CLAUDE.md → STATUS §0+§3+§10 → SCRATCH → MEMORY → board_log.tsv → inbox/WALTER/ scan → targeted owner reads (BROCK/LIQUID/REGINALD as needed). Total: 5-7 reads before execution.

**Closeout:** STATUS write-back → research detail to research/ → SCRATCH rewrite → MEMORY promotion scan → MAINTENANCE log if structural change → cross-agent outbox (acute only) → pathspec commit (no push).

**Inbox-signal:** WALTER lane: read → disposition → board_log.tsv append → `git mv` to processed/. Non-WALTER inbox: process only when spawned or triage-relevant.

**Research→canonical promotion:** findings → research/ detail file → summary row added to STATUS §2 or §3 → thesis-level finding → STATUS + MEMORY → transferable lesson → auto-memory (then remove from MEMORY.md).

**Verification-calibration:** primary/statutory filings beat media summaries; stale-mark beats carried-forward-as-current; retract in §0 when inverted; tag every figure with obs-date and source type (e.g., "T+123 [May'26 deck, JPM data]"). Peer-relative sub-row mandatory alongside absolute thresholds.

---

## 5. Self-Assessment

**STRENGTHS (most reusable):**

- **Numbered §-section STATUS model with a §0 boot-delta:** the verified threshold table at §0 (green/yellow/red per vector, with retractions) lets a cold-boot agent orient in 2 minutes without reading the full document. The §10 trigger-gated pre-registered lane (not calendar-driven) is a clean pattern for "I know what to do next but won't do it until the trigger fires." Both patterns should be portable to any agent with a live-dashboard STATUS.
- **Statutory provenance tree (`sources/`):** MANIFEST.md + dated subfolder + raw text extracts = traceable primary chain. Other agents citing secondary sources (media, third-party summaries) without a raw-primary anchor are exposed to the "just-read artifact frame contamination" failure mode.

**FRICTION (worst point):**

- **`git mv` vs bash-mv residue:** today's session committed the processed/ copy but left a dangling unstaged deletion — required a separate cleanup commit. The failure mode is subtle: `git mv` stages both add+delete atomically; bash `mv` only moves bytes and leaves git tracking the old path as "deleted (unstaged)." The lesson is in auto-memory (`git_mv_for_inbox_processing`) but didn't prevent the error. A pre-closeout `git status -- AGENTS/SHADE/` check would catch this before it becomes a push-train problem.
- **5 unprocessed WALTER signals in `inbox/WALTER/`:** SIG-W-20260622-001, -002, -624-001, -624-005, -624-009 — four of which BROCK has already acted on. SHADE's WALTER intake runs only on explicit spawn; signals accumulate between sessions.

**GAPS:**

- `NEXUS_BRIEF.md` not built — cross-agent synthesis output is ad-hoc (outbox SIGs) rather than a standing summary.
- `domain/sources/` 8 KB docs are Mar'26 vintage; no refresh cadence defined. Risk: a boot reads stale KB as current.
- No automated cadence check on `board_log.tsv` vs `inbox/WALTER/` — relies on manual scan at boot.

---

## 6. Top 3 Improvement Ideas (ranked)

1. **Add a pre-closeout `git status` sanity check as a mandatory closeout step** (before commit, after writes): `git status -- AGENTS/SHADE/` catches dangling deletions, unstaged new files, and accidental changes in other dirs — prevents the bash-mv residue class of errors. Cost: 5 seconds. Prevents a separate cleanup commit in every push-train window.

2. **WALTER INBOX AUTO-TRIAGE at boot:** process all unread `inbox/WALTER/` signals during boot (not only on explicit spawn), minimum disposition=`noted`. Currently 5 signals are sitting unread; BROCK has already acted on the insurer-lender one (SIG-005). Boot-time triage would have caught this before BROCK's action and let SHADE absorb it first.

3. **`domain/sources/` staleness flag:** add a `LAST_REVIEWED` field to each KB doc header; boot protocol checks if any KB doc is >60 days old and flags it in §0. Prevents stale KB from silently contaminating session analysis.
