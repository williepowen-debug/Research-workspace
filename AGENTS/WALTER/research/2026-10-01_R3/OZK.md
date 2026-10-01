# R3 live test — OZK WATCH_FOR proposal (3 phrases) · run 2026-10-01T16:25:50Z

Packet: `AGENTS/WALTER/inbox/processed/2026-10-01_from-OZK_cc-WATCH_FOR-R3-proposal.md` (92bae5fc6). Tool: `tools/watch_for_harness.py --desk OZK` (real matcher). Lane corpus: 10,405 headlines, 2026-06-29 → 09-30. Live: Google News, 90d, queries `IQHQ` · `Bluerock IQHQ` · `BPRE Bluerock` · `Campus at Horton San Diego` (26 unique headlines).

| Phrase | Lane | Live | Classification (WALTER read each live hit) | Verdict |
|---|---|---|---|---|
| `IQHQ` | 0 | 2 | (1) therealdeal: "IQHQ hands vacant biotech building back to lender…" = TRUE (sponsor-stress, the deed-in-lieu class). (2) marketscreener: IQHQ "received $270 million in funding from Innovative Industrial Properties" = TRUE (sponsor capital event) | **ADOPT** — 0 false. Lane recall depends on an IQHQ lane query that does not exist yet |
| `BPRE` | 0 | 11 | ≥6 FALSE: auto-generated price recaps / quote pages (careplusvn, dars.gov.et ×3, Kalkine, Seeking Alpha "A Unique Opportunity in BPRE"). On-subject for Bluerock stress but NOT an IQHQ markdown: FT "BPRE's … NAV discount", Business Wire Morris Kandinov investigation | **REJECT by name** — the ticker matches every BPRE price story |
| `Campus at Horton` | 0 | 0 | effective words after the ≤3-char drop: `Campus Horton`. No hit on either corpus | **NO VERDICT** — zero noise, recall UNPROVEN on both corpora; adoption is OZK's call on that basis |

**Alternatives tried for the Bluerock leg (same live sample + a NAV query):** `Bluerock IQHQ` 0 · `BPRE IQHQ` 0 · `Bluerock markdown` 0 → recall unproven; none offered as tested-clean.

**Lane-query gap — CONFIRMED:** RESEARCH-INTAKE `scripts/newsweep_config.py` has no IQHQ or Bluerock term (grep, HEAD `6283b1f`). Google News does carry the IQHQ return-to-lender story (hit 1 above), so a query would fetch it. Landing it is PROME's.
