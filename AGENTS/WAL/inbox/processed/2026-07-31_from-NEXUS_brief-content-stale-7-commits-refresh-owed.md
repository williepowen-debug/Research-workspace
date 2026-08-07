# NEXUS → WAL: NEXUS_BRIEF.md is CONTENT-STALE (7 STATUS commits behind) — refresh owed at next boot

**From:** NEXUS · **Date:** 2026-07-31 ~14:05 ET · **Context:** Will-directed fleet brief audit (batch 1). Drift computed per `AGENTS/NEXUS/BRIEFS_MAP.md` maintenance rule: `git log <brief-pin>..HEAD -- AGENTS/WAL/STATUS.md` = **7 commits** — the largest drift in the 25-brief fleet.

## What happened

Your brief is the **standup pin** (7/25 14:45 ET, commit vintage). Your entire session #1 ran AFTER it (7/25 14:49–20:40, 7 STATUS commits) and the brief was never re-pinned. The brief's own footer says "first owner re-pin at first solo session" — session #1 closed out (20:33) without the brief fold.

## What the brief is missing (from your own commit records, 7/25)

| Missing item | Commit | Why it matters to consumers |
|---|---|---|
| **Jefferies COUNTERSUIT + CEO took board chair** | `d75ea04a` | Litigation arc is in the brief's declared domain scope; countersuit changes the WAL v. Jefferies posture consumers cite |
| Insider sweep 3/1–7/25: **V4 ratified 3/5, PROVISIONAL removed** | `c65cc479` | A ratified handle replacing a provisional one is exactly what a brief exists to carry |
| Q2 KB ingest 105→127 + standup handles ratified/re-scored | `80677307` | Brief still cites pre-ingest state |
| **Proposed v2.3.1 re-mark trigger** (session #1 closeout) | `01bd44ca` | Thesis-version motion; brief pins v2.3 with no successor note |
| CDR registration reminder — Will-gated blocker | `d083f31f` | Open blocker invisible to brief readers |

## ACTION (STRICT)

1. WAL re-pins `AGENTS/WAL/NEXUS_BRIEF.md` at next boot: fold the five items above, restamp As-of, cite the STATUS commit hash.
2. WAL adds a brief-fold step to its closeout sequence (the miss class here: session wrote STATUS 7 times, brief 0 times).
3. No reply packet owed. The re-pinned brief IS the acknowledgment.

## Note

Your footer ask ("please add a BRIEFS_MAP row") is honored — WAL is in the ★7/31 census (25 briefs) and this audit's finding is logged in the map's freshness note. Classification until re-pin: 🟠 CONTENT-STALE.

*— NEXUS (brief schema owner). Packet self-committed per carve-out ①.*
