# OSPREY SCRATCH — 2026-07-21 AM

**Purpose:** Ephemeral session handoff — canonical "where are we / what next." Read at boot (step 2), rewritten in full at closeout. Disposable. Learnings → `MEMORY.md`; cross-agent twin → `NEXUS_BRIEF.md`.

---

## CURRENT MARKS (one line)
- Channels: refineries/products **4 🔴** (band 25-35% DEFENDED vs CARL's 42.7% GS-relay) · crude-export terminals **3 🟠 — ACTIVE WATCH: CPC Black Sea loading HALTED 7/21** (Upgrade Trigger NOT fired) · shadow-fleet tankers **3 🟠** (OSP-01 65%, unfired) · Brent ref [defer to BRENT, not re-verified].

## CHANGES SINCE LAST SESSION (7/12 PM → 7/21 AM)
- **CPC Black Sea terminal loading HALTED 7/21** after 4 tanker drone strikes in 4 days (7/18-21). Real barrels-offline, but PRIMARILY KAZAKH crude (not Russian; not OSP-01), SPMs officially undamaged → base-case DAYS. Channel-2 first genuine barrels-offline suspension since 7/12; Upgrade Trigger NOT fired.
- Vessel campaign extended Azov→Black Sea (Bloomberg 7/16, ~20 vessels incl 2 Russia-linked tankers 'hit' not sunk); stuck-at-sea/buyer-hesitancy mechanic (~135M bbl loaded-not-delivered) — SUPPORTS OSP-01, unfired.
- CARL surfaced 42.7% refining-offline → verified = Ukraine-GS self-report (7/4, design-capacity-disabled), band DEFENDED at 25-35% (Reuters ~17% + Kpler ~3.8mb/d corroborate).

## WHAT I DID THIS SESSION (fan-out spawn, CPC-focused)
- **Task 1:** verified + sized CPC halt (WALTER SIG-004). Memo → `outbox/2026-07-21_to-PROME_cpc-halt-sizing.md` + `domain/energy-strikes/CPC_HALT_2026-07-21.md`. STRIKES row RU-20260721-CPC-NOVOROSSIYSK; KB-OSPREY-012 (event) + 013 (Nov-2025 precedent). STATUS ACTIVE block + Channel-2 row updated. Proposed Channel-2 tripwire (for Will, not self-registered).
- **Task 2:** cleared full inbox backlog (WALTER 012/012-corr/018/004; PROME notes ×3) → processed/. Replies → `outbox/2026-07-21_to-PROME_inbox-triage-replies.md`: lane-query ratified w/ amendment; band defended; OSP-04 queued. board_log ×3 rows; KB-OSPREY-014 (vessel extension) + 015 (band defense).
- ⚠️ **NOT done:** full 7/12→7/21 strike-ledger gap-sweep — this was targeted CPC verification only. Swept-complete mark stays **7/12**.

## NEXT SESSION (dated, future-verifiable)
1. **Full 7/12→7/21 strike-ledger gap-sweep** (owed; mark still 7/12 — do not trust as complete). Day-by-day, mechanism-level, per LESSONS.md.
2. **CPC halt follow-through:** did SPM assessment confirm damage? Did suspension sustain ≥5 sessions / Kpler show a CPC liftings drop / Tengiz declare FM? Any = Channel-2 Upgrade Trigger fires → 🔴 BRENT.
3. **Register OSP-04** (floating storage / Urals discount / tanker congestion — stale single-vintage inputs, PROME 7/12 queue-add).
4. **By 2026-07-31 (grade 8/3):** OSP-02 resolves (diesel-ban extended/lifted).
5. **By 2026-08-02:** OSP-03 — independent >40%-offline confirmation (band expires, re-derive).
6. **By ~2026-07-26:** slow-aggregate re-verify (floating storage, Urals discount) — 14-day trigger overdue.

## OPEN THREADS / WATCHES
- 🟠 **CPC halt** — ACTIVE Channel-2 watch, base-case days; tail = weeks on confirmed buoy damage / insurer pullback (Nov-2025 SPM-2 → ~2mo + Tengiz FM precedent). **Tripwire LIVE = `GATE-OSPREY-001`** (PROME/GATES.tsv commit 2d54ba96): fire legs (a) SPM buoy structural damage / (b) suspension ≥5 sessions OR Kpler CPC liftings drop / (c) Tengiz FM → I adjudicate + 🔴 BRENT via PROME. Check these each boot while halt is live.
- 🟠 OSP-01 (Aug 1) — tanker campaign world-crude test, 65% attritional (Black Sea extension supports, unfired).
- 🟠 OSP-03 (Aug 2) — independent >40%-offline; band DEFENDED at 25-35% this session.
- 🟡 OSP-02 (Aug 3 / Jul 31) — diesel-export-ban extension.
- 🟡 Backlog: OSP-04 register, full gap-sweep, strike-feed automation, vol/credit FLOW rows, EU/Druzhba.

## PREDICTIONS DUE / DECISIONS PENDING
- None due today (OSP-01/02/03 windows all future). No Will-decision pending — OSPREY holds no trade book. One proposed tripwire (Channel-2) awaiting Will registration.

## MAIL STATE (one line per surface)
- Inbox (root): CLEARED — 3 PROME notes → processed/.
- WALTER lane: CLEARED — 4 signals → processed/.
- Outbox: 2 notes to PROME this session (cpc-halt-sizing, inbox-triage-replies) — 🟠, awaiting PROME routing.

## PENDING PUSH / GIT
- This session's files committed pathspec `AGENTS/OSPREY/` from repo root. **No push** (PROME sweeps at closeout). Tree had another session's uncommitted memory files outside my dir → did NOT pull (per protocol).
