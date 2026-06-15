# BOND SCRATCH — 2026-06-15

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next." Read at boot, rewritten in full at closeout. Disposable. Persistent learnings → `MEMORY.md`; durable thesis → `thesis/THESIS.md`; live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION (6/9 → 6/15)
- Long-end episode **relaxed**: 10Y 4.53→4.47, 30Y 5.01→4.97, VIX 21.2→16.1, DFII10 2.21 (6/10 peak)→2.16. Brent −13% (Hormuz war-risk premium out).
- **June refunding cleared**: 3Y (6/9) solid (BTC 2.64); 10Y (6/10) strong (BTC 2.57 / ind 78.0% / PD 9.4%); 30Y (6/11) soft-orderly (BTC 2.33 / ind 59.8%). No demand hole.
- Credit calm: HY 271, CCC 948, IG 74. Bifurcation didn't widen.

## WHAT I DID THIS SESSION
- Built `thesis/` structure: THESIS v1.0 + CHANGELOG + PREDICTIONS moved from workbook/ (Packets 1, 3).
- Slimmed STATUS 150→102 lines with compact-exit block (Packet 2, cde270ce).
- Resolved **BND-08 FALSE**; added **BND-09** (6/16 20Y, stress bar BTC<2.40).
- VX-BND-12/13/14 → 2, refreshed 15 evidence; aligned suite to DFII10 2.21 peak (Packet 4, 3dd74347).
- CLAUDE.md path fix (PREDICTIONS → thesis/).
- Tier-1 promotion in progress (Will-confirmed; ORC drafting Packets 7-8).

## NEXT SESSION (dated, future-verifiable)
1. **6/16 (Tue) ~1pm ET — 20Y reopening (CUSIP 912810UV8):** grade vs BND-09 (tail >1.5bp + ind <60%, or BTC <2.40). Stress marker → TLT add re-arm + long-end re-escalate.
2. **6/17 (Wed) 2pm ET — FOMC:** long-end / term-premium consequence read; rate-expectations routed to HENRY.
3. **6/18 (Thu)** — 4Y10M TIPS reopen.
4. Re-check **energy HY OAS** (stale 285 / Apr 28, owned by LIQUID) now that VIX/Brent eased.
5. Parity build remaining: Packets 6 (docket + archive), 7 (NEXUS_BRIEF + SIGNAL_INTAKE), 8 (PROME promotion), 9 (CLAUDE.md modernization).

## OPEN THREADS / WATCHES
- 🟡 Long-end re-escalation watch — **RELAXED, re-armable** at 6/16 20Y / 6/17 FOMC.
- 🟡 Credit bifurcation — CCC 948, energy HY stale (pull LIQUID).
- 🟡 VX-BND-15 anchoring — 2bp under band; candidate for →1 if breakevens keep easing.
- ⚪ Treasury buyback long-end accept-cap — YCC-lite bright-line; not current policy.

## POSITION DECISIONS PENDING
- **TLT puts:** HOLD, no add. Conditional-add re-arm on a weak 6/16 20Y or sustained 5-session threshold break.
- **HYG $75P Jun:** near-expiry salvage; reopen only on HY OAS >300 w/ velocity.

## MAIL STATE
- Inbox: clear.
- Outbox: clear (last outbox 6/5).

## WORKBOOK / PUSH HEALTH
- PREDICTIONS now in thesis/ (BND-08 resolved, BND-09 open). VX refreshed. KB/FLOW untouched this session.
- **PENDING PUSH (BOND-only, all commits f16c6b5c..HEAD):** through Packet 4 = 7 commits (f16c6b5c · 982ca50b · 7f2a8602 · 7dcf4721 · cde270ce · 6f257b91 · 3dd74347) — each verified BOND-only (0 swept files). This SCRATCH + remaining packets (5B/6/7/9) add more; use `git log AGENTS/BOND/ d69ba97e..HEAD` for the live set.
- **CONCURRENCY:** BROCK is committing in this same clone this session (disjoint dir — no conflict). A coordinated push sweeps both agents' work (push-train). With BROCK active, use **path-scoped commits** (`git commit AGENTS/BOND/<file>`), never plain `git commit` of the index — avoids the concurrent-stage race.
