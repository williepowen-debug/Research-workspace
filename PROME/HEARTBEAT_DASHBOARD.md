# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Eighteenth base 2026-09-17 (evening): **chain 1 — Amendment #1 (2026-09-18 10:3x ET: BOJ +25bp 7–2 with the yen weaker anyway · first clean SOFR/IORB pair −5bp · 9/17 credit cells flat) projected below.** *(prior: chain 0 at the base)* The seventeenth base's Amendments #1 (L404 TIPS-R grade), #2 (L271 FR2004 stock leg + pairing-date correction) and #3 (L271 funding leg) were FOLDED INTO THE BASE at the ~21:5x ET re-base and their three projections REMOVED (prose record: cold §17.2; blocks verbatim at cold §A16–§A18).*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "e3779c43e06bb0892913e912ce90abd3cadd4d62e0f29b6ae88fcfd1de24b41b",
  "set": {
    "one": "September 18, 10:3x: BOJ hiked +25bp to 1.25% on a 7–2 vote (two for HOLD) and the yen weakened anyway — USD/JPY 157.86 intraday, the 160 gate still VOID. First clean post-hike funding pair: SOFR 3.85 − IORB 3.90 = −5bp; the −28bp mixed-date figure is dead. Credit flat on the 9/17 cells (HY 270, CCC 1,076). FRED's newest H.15 cell is still 9/16 (DGS10 5.01, DFII10 2.68). Intraday: TLT $81.21 (−0.7%); VLO and USO both green ahead of Will's own VLO entry (his hands, WQ-213). Dealers short gamma into today's ~$6T opex, no wall publishable. $0 moved by PROME; STAND DOWN holds.",
    "channels": {
      "Japan / carry": {
        "headline": "🟠 BOJ HIKED +25bp to 1.25%, 7–2; the HOLD surprise did not print and the yen is WEAKER anyway — USD/JPY 157.86 intraday; 160 gate VOID",
        "body": "BOJ +25bp to 1.25% (highest since 1995), vote 7–2 (Asada · Sato for HOLD), upside inflation risk cited [BOJ k260918a.pdf; CNBC · Japan Times 9/18]. USD/JPY 157.86 [9/18 10:21 ET] from 156.26 [9/18a] / 155.57 [9/17p]. SAM dark — its vote-split pre-registration is its own grade (L34). The 160 gate is VOID, not re-armed; book FLAT; SAM V5 stands.",
        "cls": "elev"
      }
    },
    "ticker": {
      "HY OAS": "HY OAS 270 [9/17] (re-arm ≥280 = 10bp; re-kill <260 ×2 = 0-of-2, 10bp)",
      "CCC": "CCC 1,076 [9/17]",
      "BB": "BB 156 [9/17]",
      "USD/JPY": "USD/JPY 157.86 [9/18 10:21 ET, intraday]",
      "SOFR": "SOFR 3.85 [9/17] (− IORB 3.90 = −5bp, first clean pair)",
      "TLT": "TLT 81.21 [9/18 10:2x intraday]",
      "VLO": "VLO 413.20 [9/18 10:2x intraday, +0.16%]",
      "USO": "USO 157.46 [9/18 10:2x intraday, +1.39%]",
      "BOJ": "BOJ 9/18: HIKED +25bp to 1.25%, 7–2 [BOJ primary]"
    }
  }
}
```

*Prior: Seventeenth base 2026-09-17 (morning): chain 3 — three Rates-channel projections, all folded at the eighteenth re-base.*

*Prior: Fifteenth base 2026-09-12: **chain 0 — no amendments.** The fourteenth base's Amendment #1 (closeout write-back 12:1x) and Amendment #2 (the Saudi MoE Petroline shutdown statement) were FOLDED INTO THE BASE at the 2026-09-12 re-base and their projections are REMOVED here per this file's own rule; the amendment blocks themselves are rotated verbatim to `PROME/HEARTBEAT_COLD.md` §A14 / §A15 (entry-crc32 3012472809 · 1121796424). **Nothing is projected until the next `> **AMENDMENT #1` block is appended to the fifteenth base** — at which point it needs exactly one numbered projection with a `source_sha256` over its exact paragraph.*
