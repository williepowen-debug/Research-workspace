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

*Twenty-fifth base — AMENDMENT #1 (2026-10-02 16:38 ET, PROME prome-96) — projection #1 (chain 0→1):*
*source_sha256: `e980ee90f4ecda98a0ff178c3e734aee080384c42aa203cebad8c1c5e2e4d1ed` (over the exact `> **AMENDMENT #1 — ...` paragraph without its trailing newline)*
*Affects: one-liner · §1 Energy · §2 Rates · §3 Credit · §4 Europe/Japan · §5-6 Equity-vol/AI · §7 Housing/Russia/Iran · §8 Metals · 16 tickers (QQQ · SPY · TLT · USO · VLO · XLE · HYG · KRE · GLD · BIZD · HBAN · TBT · APO · WAL · FLG · MU); fire-ledger: GATE-BRK-R2 leg (a) fire #2 OCIC, GATE-BRENT-COT-35B #8 JOINT NOT-SPENT.*
*Size: HEARTBEAT 31,554 B after this amendment (97% of 32,550 B cap); 26th re-base owed next PROME session. UNREVIEWED as every amendment is.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "e980ee90f4ecda98a0ff178c3e734aee080384c42aa203cebad8c1c5e2e4d1ed",
  "set": {
    "one": "🔴 C-36 TWO-PART REAL-YIELD REGIME READ LOAD-BEARING ACROSS 3 DESKS ON 10/02 DATA: BOND EOD curve 10Y 5.28 CLOSED 4bp ABOVE pre-NFP 5.24 / 30Y real 3.34 NEW CYCLE HIGH / BE flat-down (real-yield-led NOT inflation-exp-led); HENRY RSP 7th-week DOWN HIT ($209.73 < $211.11; ties only prior ≥7-week run since 2003 = Apr-May 2022) + Sep ISM Prices-Paid 77.9 THROUGH RED; VULCAN RSP−SPY 63d went +3.7pp → −5.07pp (3.7th pctile) in 30d, 2.43pp from red band. WQ-357 analytical read UPGRADED to STRONGLY STRENGTHENED (procedural rec UNCHANGED = REAFFIRM EXIT per kill rule); Lean A window closed 15:00 UNUSED. Oil: G7 adopted ~100M bbl diesel/crude release (10:22 ET); VLO-HELD-01 leg A NOT STOOD DOWN ($99.61 vs $90.16/$95); BRENT COT-35B #8 JOINT NOT-SPENT (shorts +8,074 WoW). Credit: HY 324 [10/01, 1 tagged print >320]; GATE-BRK-R2 leg (a) FIRED #2 OCIC (counter: requests falling 21.9→18.8→16.8%); GATE-LIQ-069 2-of-2 unchanged. Housing: HOMER PMMS HOLD; kill rail 0/5; Lennar/Millrose captive-spinoff story (Hunterbrook SHORT). Metals: MIDAS gold 97.81th pct DE-crowding not UN-crowding. $0 moved by PROME; Will held through 15:00 ET UNUSED."
  }
}
```
