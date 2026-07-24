# OSPREY SCRATCH — 2026-07-24 mid-morning (day-5 check spawn — GATE FIRED)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next." Read at boot (step 2), rewritten in full at closeout. Disposable. Learnings → `MEMORY.md`; cross-agent twin → `NEXUS_BRIEF.md`.

---

## HEADLINE: GATE-OSPREY-001 FIRED 7/24
Leg-(b) branch-1 (loading suspension ≥5 sessions) fired. Halt continuous 7/20→7/24, no resumption at any point. Legs (a) SPM structural damage and (c) Tengiz FM remain UNFIRED — this is a **duration/persistence** fire, not a severity-escalation fire. Verified `date -u` at spawn = Fri 2026-07-24 14:49 UTC = 19:49 Almaty — Kazakh Friday had effectively run its full course with no resumption reported.

## CURRENT MARKS (one line)
- Channels: refineries/products **4 🔴** (band 25-35%) · crude-export terminals **4 🔴 — GATE-OSPREY-001 FIRED (leg-b branch-1, day 5)** · shadow-fleet tankers **3 🟠** (OSP-01 65%, unfired) · Brent ref [defer to BRENT].

## CHANGES SINCE LAST SESSION (7/23 midday → 7/24 mid-morning)
- **GATE-OSPREY-001 FIRED.** Day-count: 7/20=d1...7/24=d5, threshold reached, no resumption in the window.
- Leg (a): still unfired — no SPM assessment result, "fully intact and operational" line unchanged since 7/21.
- Leg (c): still unfired — no Tengiz FM; production cut still framed technical.
- **NEW:** named tanker owners (ExxonMobil, Chevron) reported refusing to call at the terminal [OilPrice.com 7/23] — owner-pullback mechanism now has named-party attribution.
- Kazakh output confirmed −21% overall / Tengiz −56% (still citing Wed 7/22 figures — no fresher production print found 7/24).
- No fresh war-risk print 7/24 (gap now spans 7/22-7/24); 7/21 figure (>1%/1.5% from 0.6%) stands.
- 7th vintage-catch this week: marketscreener "CPC resumes oil intake" headline, 403-blocked, contradicted by every live 7/24 primary — not banked.

## WHAT I DID THIS SESSION (scoped day-5 gate spawn, PROME-tasked)
- Day-5 adjudication: verdict FIRED, leg-(b) branch-1. Leg-by-leg + evidence → `domain/energy-strikes/CPC_HALT_2026-07-21.md` §9.
- Outbox → PROME: `outbox/2026-07-24_to-PROME_cpc-day5-adjudication.md` (verdict + routing asks: GATES.tsv update, BRENT routing).
- **BRENT fire-alert packet drafted and committed** (self-authored-packet carve-out): `AGENTS/BRENT/inbox/2026-07-24_from-OSPREY-via-PROME_cpc-fire-alert.md`.
- STATUS.md updated: top-line summary, gate day-count line, Channel-2 dashboard row (score 3🟠→4🔴). Flagged a stale wording mismatch in the Channel-2 "Upgrade Trigger" column (said "sustained multi-week halt" — the actual frozen GATES.tsv term is ≥5 sessions; noted inline, did not silently overwrite).

## NEXT SESSION (dated, future-verifiable)
1. **PROME to apply GATES.tsv state = FIRED** (shared file, outside my commit scope — flagged in outbox, not self-applied).
2. **PROME to finalize/confirm delivery of the BRENT packet** (already sitting in BRENT's inbox under the carve-out).
3. Watch for: (i) any SPM assessment result (leg a — would be the real severity escalation), (ii) formal Tengiz FM (leg c), (iii) resumption over the weekend (does not un-fire the already-crossed threshold, but matters for forward duration/sizing — track as a new data point, not a gate reversal).
4. War-risk print gap now 3 sessions stale (7/22-7/24) — check for a fresh Black Sea rate print next session.
5. **Register OSP-04** (stale single-vintage inputs DARK mark) — owed since 7/12, still not done.
6. By ~2026-07-26: slow-aggregate re-verify (floating storage, Urals discount) — 14-day trigger overdue.
7. By 7/31-8/3: OSP-02 resolves (diesel ban); by 8/2: OSP-03 + band expiry.

## OPEN THREADS / WATCHES
- 🔴 **GATE-OSPREY-001 FIRED** (7/24) — leg-(b) branch-1. Legs (a)/(c) open watches: any SPM assessment, any Tengiz FM.
- 🟠 War-risk surface live, print gap 7/22-7/24 (3 sessions stale) — no thresholds, route rule only.
- 🟠 OSP-01 (Aug 1, 65%) · OSP-03 (Aug 2, 35%) · 🟡 OSP-02 (Jul 31/Aug 3, 70%).
- 🟡 Backlog unchanged: OSP-04, strike-feed automation, vol/credit FLOW rows, EU/Druzhba.

## PREDICTIONS DUE / DECISIONS PENDING
- None due today (OSP-01/02/03 windows future). Gate has now resolved (FIRED) — no further adjudication needed on GATE-OSPREY-001 itself; downstream watch on legs (a)/(c) continues informally.

## MAIL STATE (one line per surface)
- Inbox (root): empty at boot.
- WALTER lane: empty.
- Outbox: **7/24 cpc-day5-adjudication** ← today's, undelivered until PROME processes (GATES.tsv update + BRENT routing confirm).
- BRENT inbox: fire-alert packet placed this session (self-authored carve-out, committed).

## PENDING PUSH / GIT
- This session's files (outbox packet, STATUS.md, SCRATCH.md, CPC_HALT tracker §9, BRENT inbox packet) committed pathspec this session and pushed via `scripts/safe-push.sh` — see commit SHA in the outbox packet / final report to PROME.
