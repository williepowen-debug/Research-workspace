# OSPREY SCRATCH — 2026-07-12 PM

**Purpose:** Ephemeral session handoff — the canonical "where are we / what next" file. Read at boot (SPAWN PROTOCOL step 2), rewritten in full at closeout. Disposable: rewritten every session, not appended to. Persistent learnings live in `MEMORY.md`; the cross-agent twin is `NEXUS_BRIEF.md`; this file is the bridge between OSPREY sessions.

---

## CURRENT MARKS (one line)
- Channel state: refineries/products **4 🔴 ESCALATED** (Omsk — Russia's largest refinery, first-ever strike) · crude-export terminals **3 🟠 UNCHANGED** (non-countable attribution holds) · shadow-fleet tankers **3 🟠 vessel-count RECONCILED** · Brent ref ~$76-79 [defer to BRENT, not re-verified this session]

## CHANGES SINCE LAST SESSION
- This IS the first live OSPREY session (prior "session" was DAEDALUS's build/spinout, not an OSPREY boot) — so "changes since" = everything found in the fresh sweep vs. the inherited 7/12 AM baseline.
- 4 material strikes found missing from the inherited ledger despite its current-dated "swept-complete through 7/12" mark: Omsk (7/6, Russia's LARGEST refinery, first-ever hit, new drone-range record), Ufa re-strike (7/1), Saratov full-halt (7/8), Syzran re-strike (7/12).
- Russia banned diesel-fuel EXPORTS entirely, 7/8 through 7/31 (Novak) — brand-new policy datum, not previously tracked anywhere in OSPREY.
- Crude exports hit a fresh record: 4.22M bpd (4wk-avg to 7/5), highest since the 2022 invasion — supersedes the 3.83M bpd figure.
- Diesel/gasoil loadings collapsed to 234kbpd (1-10 Jul) vs 817kbpd 2025-avg.
- Shadow-fleet vessel-strike claim spread (21/35/42) reconciled — daily tallies sum consistently, not contradictory.
- NO new crude-export-terminal strike found — Channel 2's non-countable attribution HOLDS, independently re-verified (not just inherited).

## WHAT I DID THIS SESSION
- Boot: read CLAUDE.md, STATUS, SCRATCH, THESIS, LESSONS, VX/FLOW/PREDICTIONS/KB, ANALYSIS, NEXUS_BRIEF, MEMORY, board_log, inbox (clean, nothing pending).
- Inheritance verification: diffed all 32 STRIKES.tsv rows, VX-HAWK-UKR-01/SHADOW-01/SHADOW-02, FLOW-HAWK-07/08/20, and OSP-01(←HAW-17) against HAWK's pre-split frozen commit (`0b172009`). Result: CLEAN — zero content defects, only legitimate spinout annotations.
- Fresh web sweep (day-by-day gap discipline, LESSONS.md item 2): found and backfilled 4 material strikes (Omsk/Ufa/Saratov/Syzran); found the diesel-export ban; refreshed crude-export and diesel-loading aggregates; reconciled the vessel-strike claim spread; flagged a 3-way non-convergence in the refining-offline aggregate.
- STRIKES.tsv: 4 new rows appended, header revised (swept-complete mark corrected with a completeness caveat).
- ANALYSIS_2026-07-12.md: regenerated with fresh aggregates, revised Watch table, updated Open-verify items.
- KB.tsv: 8 new rows (KB-OSPREY-001..008).
- VX.tsv: VX-HAWK-UKR-01 row updated with a [Jul 12 OSPREY FIRST LIVE SWEEP] entry.
- PREDICTIONS.tsv: OSP-01 confidence nudged 60%→65%; two new predictions registered (OSP-02 — diesel-ban extension, by Aug 3; OSP-03 — independent >40%-offline confirmation, by Aug 2), per the GAPS lens.
- LESSONS.md: new item added — "a swept-complete DATE is not proof of swept-complete CONTENT" (this session's own incident, distinct from the founding HAW-15 lesson).
- MEMORY.md: short addendum pointing to the new LESSONS.md item.
- Ran the 4-lens domain sweep (`PROME/packets/DOMAIN_SWEEP_LENSES.md`) across the whole corpus including inherited seed material — 12 items found, report at `reports/2026-07-12_domain-sweep.md`.
- STATUS.md: fully rewritten to reflect the independently-verified state (was HAWK-inherited/unverified going into this session).
- R1 committed as `945efa71`; route-outs DELIVERED by PROME (diesel ban→CARL, crude record→BRENT, Omsk→HAWK, steelman→RED — PROME commit 40357f1d).
- **ROUND 2 (PROME-directed, same session):**
  - EXIT RULES firmed to **v1.0** in CLAUDE.md: two-leg channel-kill rules with measurable resolvers + source tiers, thesis-kill incl. a model-falsification clause (world-crude event without Brent repricing = framework broken, escalate don't patch), prediction-retirement paths for OSP-01/02/03 (incl. VOID paths + the relay≠verification rule for OSP-03), 5-tier time-based review triggers.
  - Ufa prior strikes VERIFIED + ROWED: 6/16 Bashneft-Novoil + 6/25 Ufaneftekhim/UNPZ (found 2 prior ops, not the 1 implied). Rows RU-20260616-UFA-NOVOIL, RU-20260625-UFA; 7/1 row Strike# 2→3. KB-OSPREY-009.
  - Saratov 1st strike VERIFIED + ROWED: night of 3/21 (Meduza/news.az). Row RU-20260321-SARATOV; 5/31 row Strike# 1→2, 7/8 row 2→3. KB-OSPREY-010.
  - Refining-offline aggregate BANDED canonically: **~30% offline, band 25-35%, early-July [EST]** — method (independent-figures-only, GS excluded), supersession rule, and expiry (8/2) registered in KB-OSPREY-011; ANALYSIS + STATUS now quote the band as THE number.
  - STRIKES.tsv now 39 rows; ANALYSIS open-verify items marked resolved; STATUS/NEXUS_BRIEF refreshed.

## NEXT SESSION (dated, future-verifiable)
1. **By 2026-07-19:** re-verify the refining-offline aggregate — has an independent outlet (Energy Intelligence, Kpler, Bloomberg, Reuters) published a fresh figure? It supersedes the KB-OSPREY-011 band outright; >40% = OSP-03 CONFIRMED + Channel-1 Upgrade Trigger fires. (Window closes Aug 2.)
2. **By 2026-07-19:** damage-escalation re-check on Channel 2 (crude-export terminals) — still the single cleanest BRENT-facing tell; unfired through both rounds today.
3. **By 2026-07-31 (grade by 8/3):** OSP-02 resolves — diesel-export ban extended or lifted; RF-government statement is the resolver; VOID if mooted (see EXIT RULES §4).
4. **By 2026-07-26:** re-verify the two slow aggregates (floating storage ~120M bbl mid-June vintage; Urals discount ~25% May vintage) — 14-day trigger per EXIT RULES §5 puts these due.
5. **Standing:** first-increment backlog (strike-feed automation, vol/credit FLOW rows, EU/Druzhba expansion) — unchanged, not blocking.

## OPEN THREADS / WATCHES
- 🟠 Crude-export terminal damage-escalation watch — the standing BRENT-facing tell, re-checked this session, still unfired.
- 🟠 OSP-01 (Aug 1) — tanker campaign world-crude-disruption test, confidence 65% attritional.
- 🟠 OSP-03 (Aug 2) — independent >40%-refining-offline confirmation, gates the Channel-1 Upgrade Trigger.
- 🟡 OSP-02 (Aug 3, effectively Jul 31) — diesel-export-ban extension test.
- ~~Ufa/Saratov implied prior-strike dating gaps~~ — RESOLVED R2 (KB-OSPREY-009/010).
- 🟡 First-increment backlog (EXIT RULES item now DONE R2; strike-feed automation, vol/credit FLOW rows, EU/Druzhba remain).
- 🟡 FURTHER THREADS from the sweep report: target-selection intentionality question (Channel 1 heavy / Channel 2 light — deliberate or capacity-constrained?); whether Omsk's new range record puts other high-value facilities newly in reach.

## PREDICTIONS DUE / DECISIONS PENDING
- No predictions due for resolution this session (OSP-01/02/03 all have windows extending past today). No Will-decision pending — OSPREY holds no trade book.

## MAIL STATE (one line per surface)
- Inbox (root): clear — verified this session, nothing pending.
- WALTER lane: clear — verified this session, nothing pending.
- Outbox: clear — no 🔴 acute signals this session (all route-outs are 🟠/🟡, delivered via this session's report to PROME for routing, not via outbox files per the acute-only outbox discipline).

## PENDING PUSH / GIT (if any)
- R1 committed as `945efa71`; R2 commit is this session's final action (pathspec `AGENTS/OSPREY/`, from repo root). No push (PROME sweeps at closeout).
