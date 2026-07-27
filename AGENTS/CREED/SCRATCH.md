# CREED SCRATCH.md — Ephemeral Session State

**Rewritten:** 2026-07-27 ~15:55 ET (post-crash recovery sitting)
**Purpose:** the *handoff* surface — "what was I in the middle of, and what should the next spawn do first." Overwritten every session. **Durable analysis belongs in `STATUS.md`; structural changes belong in `MAINTENANCE.md`; nothing here is canonical.**

> **Why this file now exists (created 2026-07-27).** An unclean shutdown hit mid-audit-sweep and CREED had **no surface that said what it was doing**. Recovery worked only because five modified files happened to be legible on disk. `LAST_COMPLETION.md` — the file that *should* have carried it — had **skipped two closeouts** and was still 7/4 vintage. Adopted from the SHADE/BROCK pattern, both of which ran this file through their own crashes today.
>
> **Canonical-truth ordering is unchanged and this file is at the BOTTOM of it:** `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/` > `SCRATCH.md`. If SCRATCH disagrees with anything above it, **SCRATCH is wrong.**

---

## 🔴 NEXT-BOOT FIRST MOVES

1. **Run the boot staleness check** (`CLAUDE.md` step 7). CREED is Tier-2; **staleness between spawns is the expected steady state, not neglect** — but refresh before citing.
2. **Check the two monthly prints first** — July Trepp DQ (~early Aug) and July SS (~mid-Aug). They resolve `PRED-CREED-001` / `-002` and are the cheapest information in the domain.
3. **`VX-CREED-9.03` office vacancy is seeded at Q1 vintage** — a clean Moody's Q2 print was not locatable on 7/27. **This is the one known-stale vector.** Q2 refresh owed; if it's still not locatable, say so out loud rather than carrying Q1 as current.
4. **Update `PREDICTIONS_SCOREBOARD.md` at resolution time, not just STATUS prose.** BROCK's `BRK-29` sat `Status=OPEN` for 5 days past its own resolve date because the narrative grade landed in STATUS and the ledger row was never touched. **Both must happen, or neither counts.**

## 🟡 STATE AT HANDOFF (2026-07-27)

- **Base case:** *selective CRE recognition accelerating* — **HOLDS.** Still **pre-bank-transmission**.
- **Convergence 23/45** (was 20/40 on the retired 8-vector basis). **Proportionally flat: 50.0% → 51.1%.** ⚠️ Do NOT "simplify" the composite by dropping S5 — it yields 20/40, numerically identical to the pre-7/27 figure **by coincidence**, and would read as "nothing changed."
- **Nothing FIRED.** No signal crossed a hard trigger 7/20→7/27.
- **Mail: both lanes CLEAN.** `inbox/` and `inbox/WALTER/` empty. All dispositions now in `board_log.tsv`.
- **Workbook: BUILT and fresh** (6 TSVs, 31 vectors, 10 predictions). Threshold bands are **FROZEN TERMS** — propose to Will, never edit.

## 🔵 OPEN THREADS (carry forward)

| # | Thread | State | Where it resolves |
|---|---|---|---|
| 1 | **ARI→Athene $9B must appear somewhere** | 2 surfaces pre-registered | `PRED-CREED-010` Athene Q2 10-Q (~Aug) · `PRED-CREED-006` MBA Q2 (~mid-Sept). ⚠️ **If NEITHER moves, the migration read needs re-derivation — not a confidence trim** |
| 2 | **ARI dissolution vote** | board-resolved ≠ approved | preliminary/definitive proxy; `PRED-CREED-005` |
| 3 | **FDIC Q2 QBP** (~late Aug) | S3's actual trigger lives here | `PRED-CREED-003` — non-owner CRE PDNA vs Q1's 3.40% |
| 4 | **BXMT Q2** | the cohort's swing name | largest office-exposed lender, −17.1%/3mo, **dividend still intact** — does it follow KREF or hold? |
| 5 | **KREF Q2 10-Q** | currently **secondary-sourced** | verify-if-load-bearing; the whole 8b credit-loss leg rests on it |
| 6 | **SHADE Weld-2 triple-decker** | **unblocked, ball is SHADE's** | my CRE flow leg was re-stamped to MBA primary 7/20 and delivered 7/27 |

## ⚪ VERIFY-IF-LOAD-BEARING (do not spend on these unless they become pivotal)

- KREF Q2 **10-Q primary** (currently secondary-sourced).
- **Meadows** occupancy / DSCR / appraisal — paywalled, unverified.
- **Seattle ~37% vacancy** vs CoStar / JLL / Cushman — definitions differ materially (direct vs total-incl-sublease).
- Whether **ARI's Q1 slide was pro-forma-for-close** (the $1.3B basis question).

## ⚫ STANDING TRAPS — re-read these before writing any number down

1. **Never cite a CRE mREIT price move without checking corporate actions first.** ARI printed **−33.4% in one session** on a total-return-*positive* day: the $3.75 return-of-capital going ex 7/16. PROME reports **five instances of this class fleet-wide on 7/27 alone.** The tell isn't "mREIT" — it's **any vehicle that returns capital** (liquidating trusts, wind-downs, special dividends, spin-offs).
2. **A real number carrying the wrong basis is the dominant failure mode**, not a fabricated number. The $1.3B was real — it was a *cash* line on a *pre-close* date, labelled "post-sale."
3. **Trepp PDF is paywalled = primary-CITED, not primary-READ.** The co-circulating **"retail 12.95%" remains UNVERIFIED — do not cite.**
4. **Do not fuse ARI→Athene with Delaware Life.** Same mechanism, **opposite disclosure quality**. SHADE's rule, adopted: the discriminator is **disclosure quality + price discovery, not affiliation** — a well-governed affiliated transfer is the **benchmark**, not corroboration. And per the fleet independence rule: **we share the ARI 8-K antecedent, so agent convergence on that framing is not extra evidence.**
5. **S5 is HOMER-owned.** Cite `AGENTS/HOMER/STATUS.md` for the MF figure. Never publish a second Trepp-MF citation.

## 📬 MAIL STATE

- `inbox/` — **CLEAN** (0 items). `inbox/WALTER/` — **CLEAN** (0 items).
- `outbox/` — holds 7/20 and 7/27 PROME memos. **7/27 cross-agent packets went straight to recipient inboxes under root `CLAUDE.md` carve-out ①, which is the correct route — they were never in `outbox/`.**
- Last logged read: 2026-07-27T15:30Z (`board_log.tsv`).
