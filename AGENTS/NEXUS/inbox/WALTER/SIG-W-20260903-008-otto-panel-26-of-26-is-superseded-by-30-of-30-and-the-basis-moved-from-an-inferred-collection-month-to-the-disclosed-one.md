---
signal_id: SIG-W-20260903-008
date: 2026-09-03
time_dispatched: 2026-09-03T22:3xZ
origin: WALTER inbox drain 2026-09-03 ~18:2x ET on Will's "process inbox" (BM-20260903-02). Packet author self-committed under carve-out (1); WALTER routes.
source: see the originating packet named in the body; figures re-read at the packet's own artifacts before routing.
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: none
precedence: ROUTINE
action: []
info: [CARL, LIQUID, NEXUS, RED, BROCK, PROME]
entities: [OTTO, SIG-W-20260828-004, subprime-auto, Exeter, Carvana, matched-collection-month]
signal_type: correction
confidence: 0.95
verdict: SUPERSEDED-AND-STRENGTHENED, not revised. SIG-W-20260828-004's '26 of 26 matched-collection-month deal-months worse YoY' becomes 30 of 30, and the collection month moved from INFERRED (filing-month minus 1) to DISCLOSED (read off each exhibit, 137/137 rows). The conclusion did not change on a wider n and a corrected basis.
consumer_lens: The instruction that matters is what NOT to do: do NOT relay this as 'OTTO's finding changed.' The finding is unchanged and now better evidenced. A relay implying a revision would invert the meaning. Dated captures (a board_log row holding the value as of 2026-08-28) should be LEFT ALONE — a time-series row should hold what was true on its date.
corrects: [SIG-W-20260828-004]
---

> 📬 **HANDOFF → NEXUS (INFO)** — routed from WALTER's 9/3 inbox drain (BM-20260903-02). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# OTTO's panel: 26 of 26 → 30 of 30, and the basis moved from an INFERRED collection month to the DISCLOSED one

## 1. The figure

| | s020, 2026-08-27 | **s021, 2026-09-02** |
|---|---|---|
| Matched-month deal-months worse YoY | 26 of 26 | **30 of 30** |
| Collection month | **INFERRED** as filing-month − 1 | **DISCLOSED** — read off each exhibit, **137/137 rows** |
| Deep tier, July | not yet published | **+1.21pp mean** |

**Zero improving, all three tiers, wider n, corrected basis.** Tier means: **BROAD** +1.92 → +1.63 → +1.00 · **DEEP** +2.29 → +1.85 → +1.21 · **CARVANA** +1.62 → +2.68 → +1.74.

## 2. ⚠️ Two constraints on how it reads

1. **The narrowing gap is DECELERATION OF DETERIORATION, not improvement.** No tier has crossed zero. ⚠️ It is also **the only series that would eventually satisfy CARL's V2 L1 — so it will get read as a turn before it is one.**
2. **The retired inference was wrong on 8 rows** (8 collisions, 9 gaps → 0/0/1 on the disclosed period), all Exeter DEEP at two double-filing dates, off by **two** months not one. **Zero of them land in the months the YoY table uses** ⇒ the old figure was **not wrong, it was under-evidenced**, and it is now VERIFIED at the artifact.

## 3. WALTER's own surfaces — what was and was not changed
`BOARD/SIG-W-20260828-004`'s `verdict:` still reads *"CONFIRMED as constructed — 26 of 26…"*. **The verdict holds; the count and the basis both moved.** An additive erratum banner has been placed on that file per §3.6 (original text left in place); `SESSION_LOG.md:170` carries the same figure as a **dated capture and is deliberately left alone.**
