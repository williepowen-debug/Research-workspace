# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Twenty-second base 2026-09-25 (post-close) — chain 0: the twenty-first base's amendment #1 was folded into the base at the re-base, so its projection is REMOVED; zero projections stood until amendment #1 (2026-09-26 17:5x ET, PROME, Will-directed correction).*

*Twenty-third base 2026-09-28 (post-close, PROME prome-64) — chain 0: the twenty-second base's amendments #1–#3 were folded into the base at the re-base, so their projections are REMOVED; three projections then accumulated (am.#1 9/28 22:1x · am.#2 9/29 10:5x · am.#3 9/29 15:5x).*

*Twenty-fourth base 2026-09-29 (post-close, PROME prome-f4) — chain 0 at the re-base; amendments #1–#3 (9/30) each carried one projection until the twenty-fifth re-base folded them.*

*Twenty-fifth base 2026-10-01 (post-close, PROME prome-2f) — chain 0: the twenty-fourth base's amendments #1–#3 were folded into the base at the re-base, so their projections are REMOVED; zero projections stand. The folded projections are preserved in this file's commit history (`git log -p -- PROME/HEARTBEAT_DASHBOARD.md`).*

*Twenty-sixth base 2026-10-02 (post-close, PROME prome-72) — chain 0: the twenty-fifth base's amendment #1 was folded into the base at the re-base, so its projection is REMOVED; zero projections stand. The folded projection is preserved in this file's commit history (`git log -p -- PROME/HEARTBEAT_DASHBOARD.md`).*

*Twenty-seventh base 2026-10-07 (post-close, PROME prome-0e) — chain 0: the twenty-sixth base's amendment #1 (the NEXUS split restored, 10/4) was folded into the base at the re-base, so its projection is REMOVED; zero projections stand. The split now renders from the base text itself (hot §5). The folded projection is preserved in this file's git history and in `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-10-07.md`.*

*Twenty-eighth base 2026-10-08 (post-close, PROME prome-7c, desktop) — chain 0: the twenty-seventh base's amendments #1 (the 30Y-real superlative, 10/8 08:34) and #2 (the ICE 10/7 cells + the 11:03 re-mark, 10/8 11:43) were folded into the base at the re-base, so their projections are REMOVED; zero projections stand. The folded projections are preserved in this file's commit history (`git log -p -- PROME/HEARTBEAT_DASHBOARD.md`) and the amendments verbatim in cold §KOS.12 and the 2026-10-08 snapshot.*

*Twenty-ninth base 2026-10-09 (post-close, PROME prome-15, desktop, crash-recovery session, installed 16:26 ET) — chain 0: the twenty-eighth base's amendments #1–#3 were folded into the base at the re-base, so their projections are REMOVED; zero projections stand. The folded projections are preserved in this file's commit history (`git log -p -- PROME/HEARTBEAT_DASHBOARD.md`) and the amendments verbatim in `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-10-09.md`.*

*Twenty-ninth base — AMENDMENT #1 (2026-10-09 17:0x ET, PROME prome-15; SAM sam-1009pm) — projection #1 (chain 0→1):*
*source_sha256: `a81fd123a0da27517caa32e130d202516db65a70bb234ea9c73c6c28529c15e4` (over the exact `> **AMENDMENT #1 — ...` paragraph without its trailing newline)*
*Affects: the Japan/carry channel only — SAM's owner grade mirrored; no gate, level or blocking row changes; the one-liner carries no yen clause on this base, so it is unchanged. UNREVIEWED as every amendment is.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "a81fd123a0da27517caa32e130d202516db65a70bb234ea9c73c6c28529c15e4",
  "set": {
    "channels": {
      "Japan / carry": {
        "headline": "USD/JPY closed 158.246 — FOURTH close above 158.054 (MET, provisional); VECTOR-5 stays NONE; nothing arms",
        "body": "SAM 10/9 17:01 ET: completed close 158.246 (London-session basis, provisional on the vendor's 17:00 ET tick; margin 0.192). Fourth close above, not first since 9/23 (9/23 · 9/24 · 10/6 · 10/9); 7-session 157.83–158.25 range, no fast leg, no intervention. VECTOR-5 (c) re-met in letter; (b) ¥16,466 vs ¥18,000 NOT MET ⇒ NONE. ¥160 VOID; book FLAT. JGB 10Y 3.111 [MOF 10/7] highest since Aug-1996 (not all-time); SAM-33 un-fired; Totan Oct 10%."
      }
    }
  }
}
```
