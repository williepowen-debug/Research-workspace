# CREED SCRATCH.md — Ephemeral Session State

**Rewritten:** 2026-08-13 ~14:20 ET (Will-directed private-credit grouping session, PROME-spawned alongside SHADE + BROCK)
**Purpose:** the *handoff* surface — "what was I in the middle of, and what should the next spawn do first." Overwritten every session. **Durable analysis belongs in `STATUS.md`; structural changes belong in `MAINTENANCE.md`; nothing here is canonical.**

> **Canonical-truth ordering is unchanged and this file is at the BOTTOM of it:** `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/` > `SCRATCH.md`. If SCRATCH disagrees with anything above it, **SCRATCH is wrong.**

---

## 🔴 NEXT-BOOT FIRST MOVES

1. **Commit the SHADE reply packet if it's still sitting uncommitted.** `AGENTS/CREED/inbox/2026-08-13_from-SHADE_PRED-CREED-010-athene-Q2-mortgage-line-FINAL-primary-figures.md` was untracked as of this session's close — it's SHADE's self-authored packet (carve-out ①), **not CREED's to commit**. If it's still sitting untouched next boot, that's fine (SHADE owns it); do not `git mv` it into `processed/` until it's tracked, and never commit content you didn't author into your own history.
2. **Check whether HOMER replied to the courier-KILL packet** (`AGENTS/HOMER/inbox/2026-08-13_from-CREED_courier-arrangement-KILLED-per-PROME-row-47-ruling.md`). No reply is expected or owed — HOMER's side needs no action — but confirm nothing came back disputing the call.
3. **August Trepp DQ/SS prints (~early/mid-Sept)** are the next real information: they're what can actually test `PRED-CREED-001` (July printed 11.91%, 9bps below the 12.00% trigger — the *fastest* MoM move since January, so August is the print to watch hardest).
4. **FDIC Q2 QBP (~late Aug) is now the single most overdue owed item** — it's S3's actual trigger and has been owed since the 7/27 session's "Owed next spawn" list. Check if it has printed before doing anything else market-facing.
5. **`PRED-CREED-006` (MBA Q2 CM/MF, ~mid-Sept)** is the item that finally settles the joint verdict with `010` (Athene leg graded PARTIAL this session, Δ +$6.9B, $103M short of LANDED). Do not grade `010` again standalone — it's already at its terminal interim state pending `006`.
6. **`VX-CREED-9.03` office vacancy is now 2 cycles Q1-stale** (flagged 7/27, still stale 8/13). If a clean Moody's Q2 print still isn't locatable, say so explicitly a second time rather than let a third cycle pass silently.
7. **Eval suite has a known defect, unfixed.** `CLAUDE.md`'s ALWAYS-LOADED traps block names ARI (trap #1) and the MBA $775B line (trap #5) verbatim, which VOIDs `case_01`/`case_02` on contamination by construction. If the next session touches the eval suite or `CLAUDE.md`'s traps block, consider whether to anonymize the traps' named entities or loosen the contamination rule to permit citing CLAUDE.md's own loaded text. Not urgent — flagged, not blocking.

## 🟡 STATE AT HANDOFF (2026-08-13)

- **Base case:** *selective CRE recognition accelerating* — **HOLDS.** Still pre-bank-transmission. Nothing fired 7/27→8/13.
- **Convergence unchanged: 23/45 (51.1%).** This session did grading + hygiene, not thesis movement.
- **Courier arrangement with HOMER: KILLED**, not heartbeat-repaired. Full reasoning in `CLAUDE.md` §S5 sourcing. HOMER's disclosed-secondary MF pull is now the sole standing method; CREED may still pass along whatever it reads opportunistically, no commitment.
- **PRED-CREED-001:** NOT resolved. July office DQ 11.91% (+34bps), still below the 12.00% trigger.
- **PRED-CREED-010:** Athene leg reads PARTIAL (Δ +$6.9B, $103M short of the $7.0B LANDED bar), reconciled to one figure with SHADE. Joint verdict with `006` still pending (~mid-Sept). Purchase price corrected to $8.7B (primary-confirmed, was ~$9B).
- **Eval suite:** first run, both cases VOID on contamination (a suite defect, not a CREED reasoning failure — see STATUS §2026-08-13 ③ for the substance read). Not re-run this session.
- **Mail: both lanes CLEAN.** All 8 pre-existing inbox items + the WALTER GSE-MF packet processed to `processed/`; SHADE's late-arriving reply left uncommitted (its packet, its commit).
- **Workbook:** VX-CREED-1.01/1.02/1.06 refreshed with the July print; VX_HISTORY appended. PREDICTIONS.tsv + SCOREBOARD updated for both graded rows. `board_log.tsv` has 11 new rows this session (9 inbox items + the SHADE reconciliation + nothing else).

## 🔵 OPEN THREADS (carry forward)

| # | Thread | State | Where it resolves |
|---|---|---|---|
| 1 | **`PRED-CREED-006`/`010` joint verdict** | 010 read PARTIAL 8/13; 006 still open | MBA Q2 print, ~mid-Sept. Grade together — one transaction, two surfaces. |
| 2 | **FDIC Q2 QBP** | owed since 7/27, now the most overdue item | S3's actual trigger — `PRED-CREED-003` |
| 3 | **`VX-CREED-9.03` office vacancy** | Q1-vintage, now 2 cycles stale | Moody's Q2 print, if locatable |
| 4 | **ARI preliminary proxy + shareholder vote** | board-resolved ≠ approved | `PRED-CREED-005` |
| 5 | **KREF Q3 / BXMT Q2** | unchanged since 7/27 | office run-off <10%? does BXMT follow KREF or hold? |
| 6 | **Eval suite contamination-check defect** | flagged, not fixed | next `CLAUDE.md` traps-block edit or next eval run |
| 7 | **SHADE's 8/13 reply packet, uncommitted** | in CREED's inbox, SHADE's to commit | watch it clear on its own; don't touch |
| 8 | **CORAL's standing FL feed** | accepted 8/3, no slice sent yet | send when a loan-level/metro Trepp pull is reachable, not from a secondary-aggregate pull |

## ⚫ STANDING TRAPS — re-read these before writing any number down

> ⚠️ **Traps 1, 2, 3, 6 and 8 are ALSO in `CLAUDE.md` §Standing traps — ALWAYS-LOADED, and that copy is the one that matters.** If you edit one here, edit it there too — and `CLAUDE.md` wins.

1. **Never cite a CRE mREIT price move without checking corporate actions first.** ARI's ex-dividend trap is the canonical example; the eval's case_01 confirmed this discipline still holds when tested cold.
2. **A real number carrying the wrong basis is the dominant failure mode**, not a fabricated number. The ARI ~$1.3B / $2.2B basis confusion is the canonical example; this session's Athene $9B→$8.7B purchase-price correction is a fresh instance of the same class.
3. **Trepp PDF is paywalled = primary-CITED, not primary-READ.** Still true — the July print came via Connect CRE's infogram + HOMER's cross-corroboration, not a direct Trepp read.
4. **Do not fuse ARI→Athene with Delaware Life.** Unchanged.
5. **S5 (multifamily) is HOMER-owned for scoring.** The DATA-PULL courier arrangement is now KILLED (8/13) — CREED no longer has a standing pull commitment at all, opportunistic only.
6. **Anchor a threshold to a DISTRIBUTION, not to the most recent number.** The eval's case_02 showed this lesson is only PARTIALLY internalized — a model can avoid the single-print anchor while still matching the wrong SEASON. Watch for this specific half-failure in future threshold-setting.
7. **Check the other side's sourcing before writing a citation rule.** Unchanged.
8. **⚠️ The MBA $775B life-insurer line is WHOLE LOANS ONLY.** Unchanged — and now also the reason case_02's eval run VOIDs on contamination (citing it by name from CLAUDE.md's own trap #5).
9. **⚠️ Do not let 99.7% be generalized into "the sink absorbs at par."** Unchanged.
10. **NEW 2026-08-13 — a band derived as a percentage of an unverified quantity silently hard-codes that quantity.** SHADE's method lesson from the Athene grade: the $7.0B LANDED bar was 78% of an *assumed* $9B deal; when the true price ($8.7B) surfaced in the same filing as the print, the band's literal value and its stated intent diverged. Register RATIOS when the denominator isn't yet verified, not levels.

## 📬 MAIL STATE

- `inbox/` — CLEAN except SHADE's uncommitted 8/13 reply (not CREED's to move). `inbox/WALTER/` — CLEAN, one item processed this session.
- `outbox/` — holds 7/20, 7/27, and this session's memo (`2026-08-13_to-PROME_private-credit-session.md`).
- Last logged read: see `board_log.tsv`, rows through 2026-08-13T14:10:00Z.
