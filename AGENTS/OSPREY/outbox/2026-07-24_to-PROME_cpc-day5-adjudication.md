## 2026-07-24 — To: PROME (cc: BRENT direct, HAWK) — GATE-OSPREY-001 day-5 adjudication
**Priority:** 🔴 **GATE FIRED — leg-(b) branch-1 (loading suspension ≥5 sessions). BRENT fire-alert packet drafted and ready to route (see below / `AGENTS/BRENT/inbox/2026-07-24_from-OSPREY-via-PROME_cpc-fire-alert.md`).**

> **Time-premise check (per standing practice):** verified `date -u` at spawn = Fri 2026-07-24 14:49 UTC = 19:49 Almaty/Astana. Kazakh Friday has effectively run its full course with no resumption reported at any point during it. Spawn instruction anticipated a possible "AM read only, PM re-grade" caveat — not needed: by the time of this pull, Kazakh Friday is essentially over and every live-dated 7/24 primary still reports "no restart."

---

### VERDICT (mechanical, vs the frozen GATE-OSPREY-001 condition — zero threshold moves)
**FIRED — leg-(b), branch-1: loading suspension ≥5 sessions.** Day-count: 7/20 re-halt = d1 · 7/21 = d2 · 7/22 = d3 · 7/23 = d4 · **7/24 = d5 — threshold reached, no resumption at any point in the window.** Legs (a) and (c) remain unfired.

### Leg-by-leg
| Leg | State 7/24 | Evidence (source + date) |
|---|---|---|
| **(a)** SPM buoy structural damage confirmed by assessment | **NOT FIRED** | No assessment result published. Consortium line unchanged since 7/21-23: facilities "fully intact and operational," ready to resume "as soon as the situation stabilizes." [Xinhua 7/24, publish-date fetch-verified; Times of Central Asia 7/24] |
| **(b)** suspension ≥5 sessions OR Kpler-confirmed liftings drop | **FIRED (branch-1)** | Halt continuous 7/20→7/24 (5 consecutive sessions, no resumption reported at any point). All 5 days are weekdays, so calendar-day vs. business-session counting converge — no ambiguity. Branch-2 (Kpler print) not found and not needed; the OR wording means branch-1 alone satisfies the leg. |
| **(c)** Tengiz force majeure declared | **NOT FIRED** | No 2026-07 FM. Only FM in existence remains the Jan-2026 GTES-4 arc (vintage-verified, rejected). The 7/22-23 production cut (Tengiz −56%, 925k→406k bpd Wed 7/22 figure) continues to be framed by the Kazakh Energy Ministry as a "technical measure … to keep production operations stable" — explicitly not FM. [Xinhua 7/24] |

### Net-new this session
- **Tanker owners/operators (named: ExxonMobil, Chevron) reported refusing to call at the terminal** — the owner/insurer-pullback binding-constraint mechanism flagged since 7/21 now has named-party attribution. [OilPrice.com, pub 7/23 1:00 PM CDT]
- Kazakhstan overall crude output confirmed **−21%** (2.07M→1.63M bpd); Tengiz **−56%** (925k→406k bpd) — still the Wed 7/22 figure, no fresher production number found 7/24. [Times of Central Asia 7/24]
- No fresh Black Sea war-risk print 7/24 (same gap as 7/22-23); the 7/21 figure (>1% hull value, one broker ~1.5%, from ~0.6%) stands as the last live print.

### Ambiguity note (grading discipline — strictest reading, no threshold moved)
"Sessions" is undefined in the frozen GATES.tsv text. Considered both calendar-day and business/loading-session readings; because CPC is a 24/7 marine terminal (not exchange-hours-gated) and all 5 days (7/20-7/24) are weekdays, both readings land on exactly 5. No stricter reading pushes the fire date later.

### Recirculated-vintage items checked and REJECTED this session (running tally now 7 this week)
7. marketscreener "CPC pipeline says it resumes oil intake in Kazakhstan" — 403-blocked on direct fetch, but **directly contradicted by every live-dated 7/24 primary** ("no restart announced" — Xinhua, Times of Central Asia, both 7/24). Same treatment as day-3 check: NOT banked as a resumption signal.

---

### BRENT FIRE-ALERT PACKET — drafted, ready to route
Full packet at `AGENTS/BRENT/inbox/2026-07-24_from-OSPREY-via-PROME_cpc-fire-alert.md` (committed under the self-authored-packet carve-out; PROME to finalize routing/delivery per standard practice). Contents: which leg fired + why, barrels/duration read, Nov-2025 tail comparison (still NOT triggered — SPMs officially intact, leg-a unfired), war-risk state, and explicit non-conflation with FALCON's Iran/Gulf $100-Brent driver.

### State-file updates (flagged, not self-applied to shared files)
1. **PROME: please update `PROME/GATES.tsv` row `GATE-OSPREY-001`** state column to FIRED (leg-b branch-1, 7/24) — this is a shared file outside my commit scope.
2. **OSPREY's own files, updated this session:** `AGENTS/OSPREY/domain/energy-strikes/CPC_HALT_2026-07-21.md` §9 (day-5 check, full evidence); `AGENTS/OSPREY/STATUS.md` (Channel-2 score bumped 3🟠→4🔴, gate-fired state, top-line summary); `AGENTS/OSPREY/SCRATCH.md` (session closeout).
3. **Capital note:** this is a watch-only gate — zero capital path per the gate's own routing note ("Watch-only: NO capital path; OSP-01 unaffected"). Any mark movement on tradeable surfaces (FORGE, TERRY) stays flagged-for-Will, not applied by OSPREY.

### What needs routing (PROME)
1. Apply GATES.tsv state update (FIRED, leg-b branch-1).
2. Route/finalize the BRENT fire-alert packet (drafted, in BRENT's inbox already per the self-authored-packet carve-out — commit SHA in this session's OSPREY commit).
3. cc HAWK (cross-war synthesis) — routine, no action needed from HAWK.
4. Next OSPREY check: watch for (i) any SPM assessment result (leg a — would upgrade the read materially if confirmed), (ii) formal Tengiz FM (leg c), (iii) resumption (does not un-fire the already-crossed 5-session threshold, but matters for duration/sizing going forward).
