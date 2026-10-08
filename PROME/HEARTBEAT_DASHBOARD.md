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

*Twenty-seventh base — AMENDMENT #1 (2026-10-08 08:36 ET, PROME prome-fc) — projection #1 (chain 0→1):*
*source_sha256: `d4aeba772c4d1e47e3b8d84628b14ac11fdaecaca7fcdf00201fa2aac27788ae` (over the exact `> **AMENDMENT #1 — ...` paragraph without its trailing newline)*
*Affects: the one-liner's 30Y-real clause and the Rates channel body — a superlative corrected (3.36 [10/7] is not the window high; 3.37 [10/5] is, FRED DFII30); no level, gate, count, ticker or blocking row changes. UNREVIEWED as every amendment is.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "d4aeba772c4d1e47e3b8d84628b14ac11fdaecaca7fcdf00201fa2aac27788ae",
  "set": {
    "one": "🔴 THE CREDIT PRINT CAME BACK UNDER THE LINE AND THE LONG END DID NOT: HY OAS 303 [10/6] after ONE 324 print [10/1] — the 10/2 cell (310) RESET the >320 count (REG-T-03 graded 0 of 3); the official 30Y closed 5.67 and the 30Y REAL 3.36 [10/7 official; the window high was 3.37 on 10/5] — while the 10Y auction cleared STRONG and the September minutes lean to ANOTHER HIKE by year-end; EIA lifted Q4 Brent to $105 (cutoff 10/1) and CUT the draws; a THIRD Cushing build; the November crack ESTIMATE $105.82 [10/7, BRENT] — nothing fires; QQQ 757.73 [10/7c] above the 10/2 record on breadth NOBODY has re-measured since 10/2; BANKS SOLD WEDNESDAY — KRE −1.7%, WAL and OZK −2.3%, FLG 11.30 BROKE REGINALD's $11.39 red rung (graded; nothing gated); the book has TWO FRIDAY EXPIRIES (QQQ 755P ×2 · USO 150C ×1, $26 [10/7 rcv]) and NEW, uncarded bank puts (WAL Dec-18 65P ×4 · OZK Nov-20 40P ×4). X1 stays CLOSED (8/28). Book mirror = the 10/7 INTRADAY capture (ANVIL e8fd99acf); NO Activity, NO fills booked. $0 moved by PROME; STAND DOWN holds (WQ-192).",
    "channels": {
      "Rates": {
        "body": "OFFICIAL Treasury [10/7, BOND]: 2Y 4.77 · 5Y 5.03 · 10Y 5.28 · 20Y 5.71 · 30Y 5.67 · 10Y real 2.92 · 30Y real 3.36 (window high 3.37 on 10/5) · 2s30s 90bp (+5 d/d). FRED H.15 [10/6]: DGS10 5.27 · DFII10 2.91; T10YIE 2.36 …"
      }
    }
  }
}
```

*Twenty-seventh base — AMENDMENT #2 (2026-10-08 11:43 ET, PROME prome-fc) — projection #2 (chain 1→2):*
*source_sha256: `705de46c76fd6c9e5e94146469252510918b51773068a5c6c2a7f39ee53b46be` (over the exact `> **AMENDMENT #2 — ...` paragraph without its trailing newline)*
*Affects: the one-liner (HY 309 [10/7] replaces 303 as the latest cell; both Friday expiries in the money at 11:03 ET with TERRY's SELL-TODAY leans and WQ-396/397; OZK's band fire named) and the Credit channel body (the 10/7 cells). No gate, level or blocking row changes — owner grades mirrored. UNREVIEWED as every amendment is.*

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "705de46c76fd6c9e5e94146469252510918b51773068a5c6c2a7f39ee53b46be",
  "set": {
    "one": "🔴 THE CREDIT PRINT CAME BACK UNDER THE LINE AND THE LONG END DID NOT: HY OAS 309 [10/7] (303 [10/6]) after ONE 324 print [10/1] — the 10/2 cell (310) RESET the >320 count (REG-T-03 graded 0 of 3); the official 30Y closed 5.67 and the 30Y REAL 3.36 [10/7 official; the window high was 3.37 on 10/5] — while the 10Y auction cleared STRONG and the September minutes lean to ANOTHER HIKE by year-end; EIA lifted Q4 Brent to $105 (cutoff 10/1) and CUT the draws; a THIRD Cushing build; the November crack ESTIMATE $105.82 [10/7, BRENT] — nothing fires; QQQ 757.73 [10/7c] above the 10/2 record on breadth NOBODY has re-measured since 10/2; BANKS SOLD WEDNESDAY — KRE −1.7%, WAL and OZK −2.3%, FLG 11.30 BROKE REGINALD's $11.39 red rung (graded; nothing gated), OZK's <$45 band FIRED (43.56 [10/7c]; the RaDD bridge matures Fri 10/9); the book has TWO FRIDAY EXPIRIES (QQQ 755P ×2 · USO 150C ×1), BOTH IN THE MONEY at 11:03 ET 10/8 (QQQ $754.27 · USO $150.27) — TERRY leans SELL TODAY, roll NONE, WQ-396/397 (Will's hand) and NEW, uncarded bank puts (WAL Dec-18 65P ×4 · OZK Nov-20 40P ×4). X1 stays CLOSED (8/28). Book mirror = the 10/7 INTRADAY capture (ANVIL e8fd99acf); NO Activity, NO fills booked. $0 moved by PROME; STAND DOWN holds (WQ-192).",
    "channels": {
      "Credit": {
        "body": "FRED [first-published, cache-busted 11:03 ET 10/8]: HY OAS 324 [10/1] → 310 [10/2] → 312 [10/5] → 303 [10/6] → 309 [10/7] · CCC 1,229 · IG 82 · BBB 102 · BB 189 · B 308 [10/7]. HY >320: ONE print (10/1); the count stays 0 (REG-T-03 owner-graded 0-of-3 at the 10/6 cell; the 10/7 cell does not restart it). GATE-HY-REKILL 0-of-2, 49bp above · GATE-LIQ-072 NOT FIRED (IG 82 vs >94; HY−IG 227 vs <180). CCC−BB gap 1,040bp [10/7] …"
      }
    }
  }
}
```
