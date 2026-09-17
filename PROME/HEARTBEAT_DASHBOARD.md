# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Seventeenth base 2026-09-17: **chain 2 — Amendment #1 (13:1x ET, DOCKET L404 TIPS-R grade) and Amendment #2 (13:2x ET, DOCKET L271 FR2004 join + the pairing-date correction) projected below.** *(prior: chain 0 at the base)* The sixteenth base (2026-09-14) carried no amendments either (its size clock fired instead); the post-FOMC rewrite of 2026-09-17 is a BASE, not an amendment, so nothing is projected here until the first `> **AMENDMENT #1` block is appended to the seventeenth base — at which point it needs exactly one numbered projection with a `source_sha256` over its exact paragraph. Pre-re-base history: `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-09-17.md` (receipt `git show 71ec15585:HEARTBEAT.md`).*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "b42e557f4faa7c6bfd3f79eaccbe3999d6950a4093db5d2beb3cf2f2a59646bf",
  "set": {
    "one": "September 17, 13:1x: the 10Y TIPS-R reopening graded CLEAN on BOND's frozen bars (BTC 2.24 · indirect 59.12 · dealer 12.18); stop 2.6530% is the highest 10Y TIPS auction stop since October 2008. Adequate demand on a held-rally session (TLT +0.90% intraday), not new bull evidence. The grading tool's I′ line for TIPS is NOT the spec — conflict deferred to the 10/1 refresh. Counter 0, no add, $0. The Fed's +25bp hike and the oil-down-on-a-restart-claim regime are unchanged; STAND DOWN holds.",
    "channels": {
      "Rates": {
        "headline": "🟢 10Y TIPS-R reopening CLEAN on frozen bars; stop 2.653% = highest since Oct-2008; I′ tool line NOT the spec",
        "body": "BOND graded 91282CRE3 (13:00 ET) on the 9/9-frozen bars: BTC 2.24 vs <2.20 · indirect 59.12 vs <56.08 · dealer 12.18 vs >17.79 — all inside. Stop 2.6530% = highest 10Y TIPS stop since 2008-10-08 (rank 15 of 140, pre-registered). Held-rally session (TLT $81.61 +0.90%, ^TNX 4.95 intraday 13:16) ⇒ adequate, not strong. grade_auction.py's I′ line (61.44) would fire and is NOT applied — TIPS excluded from I′ by the pre-print spec; decision at the 10/1 refresh (KB-BND-304). Directs backfilled twice running (masked-hole shape, n=2, no fire: dealers below trailing-12 maxima). Counter 0; no add; FR2004 join 9/18 remains the critical path. The base's other Rates facts (hike in, SEP below the curve, DFII10 2.62 [9/15], 007 0-of-5) stand."
      }
    }
  }
}
```


*Prior: Fifteenth base 2026-09-12: **chain 0 — no amendments.** The fourteenth base's Amendment #1 (closeout write-back 12:1x) and Amendment #2 (the Saudi MoE Petroline shutdown statement) were FOLDED INTO THE BASE at the 2026-09-12 re-base and their projections are REMOVED here per this file's own rule; the amendment blocks themselves are rotated verbatim to `PROME/HEARTBEAT_COLD.md` §A14 / §A15 (entry-crc32 3012472809 · 1121796424). **Nothing is projected until the next `> **AMENDMENT #1` block is appended to the fifteenth base** — at which point it needs exactly one numbered projection with a `source_sha256` over its exact paragraph.*

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "f13cc9a3320df9b42c54ac180b155eb0ad5321186e96e196ae9570da51eb794f",
  "set": {
    "one": "September 17, 13:2x: BOND's FR2004 join landed early and the paired thesis-kill INVERTS — paired I′ fires run to lower yields, unpaired to higher (p=0.009); BOND is not proposing the looser kill it favours, and the funding leg is untested. Leg ② is Will's (WQ-157, 9/19; PROME rec PARK). Date correction: the 9/15 20Y fire pairs ~early October, not 9/18. Earlier today the 10Y TIPS-R reopening graded CLEAN (stop 2.653%, highest since Oct-2008; adequate demand on a held-rally session). Counter 0, no add, $0; STAND DOWN holds.",
    "channels": {
      "Rates": {
        "headline": "🟠 FR2004 join: the paired kill INVERTS (p=0.009); leg ② to Will, PARK rec; 9/15 fire pairs ~early Oct, not 9/18",
        "body": "BOND's WQ-157 leg ② join (88c891470, n=244 prints, 224 joined auctions): I′ standalone fires 23.2%, old conjunctive 1.8%; the best dealer-stock leg separates by only +11.8pp (p=0.137) and PAIRED fires precede LOWER yields (−5.0bp, 27% rising, n=30) while unpaired precede HIGHER (+6.5bp, 68%, n=22). BOND disclosed the direction (a looser kill confirms its thesis) and proposes nothing; SOFR−IORB leg untested, now being built. The 9/15 20Y-R I′ fire cannot be paired until the 9/16 FR2004 as-of publishes (~early October) — 9/18 was the instrument's date. Earlier: 10Y TIPS-R CLEAN on frozen bars, stop 2.653% highest since 2008-10-08, adequate not strong; I′ tool line for TIPS not the spec (10/1). Base facts stand: hike in, SEP below the curve, DFII10 2.62 [9/15], 007 0-of-5."
      }
    }
  }
}
```
