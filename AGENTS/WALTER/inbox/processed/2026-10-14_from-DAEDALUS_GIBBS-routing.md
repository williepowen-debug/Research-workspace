# DAEDALUS → WALTER — new desk GIBBS (large banks): routing lane

**From:** DAEDALUS · **Written:** 2026-10-14 21:11 ET · **Ruling:** WQ-426 (Will 10/14, "Approve 426 and 427" / "yes, build it") · **Charter:** `AGENTS/GIBBS/CLAUDE.md` · **Perimeter (canonical):** `AGENTS/GIBBS/workbook/PERIMETER.tsv` · Priority 🟡

GIBBS is a Tier-2, event-driven desk over 16 named US banks. It asks two questions: is regional-bank stress industry-wide or regional-only, and is large-lender lending to non-bank finance transmitting it. Its first session is Mon 10/19 (PROME spawn).

- **ACTION:** Add a GIBBS lane to `ROUTING_TABLE` and the `FORMAT_SPEC` routing fields for these tickers: JPM · BAC · C · WFC · GS · MS · BK · STT · AXP · NTRS · USB · COF · PNC · TFC · SCHW · FITB.
- **ACTION:** Map these aliases to the same lane: JPMorgan · Bank of America · Citigroup / Citi · Wells Fargo · Goldman Sachs · Morgan Stanley · BNY / BNY Mellon / Bank of New York Mellon · State Street · American Express / Amex · Northern Trust · U.S. Bancorp / US Bank · Capital One · PNC · Truist · Charles Schwab / Schwab · Fifth Third.
- **ACTION:** Route these topics to GIBBS (cc REGINALD): Fed tailoring thresholds or their re-indexing · stress test / stress capital buffer · GSIB surcharge · the capital re-proposal (AOCI for Cat III/IV) · large-bank deposit costs, CRE/office reserves, NII guidance.
- **cc rules:** NDFI / private-credit items at these names → BROCK primary, cc GIBBS (one figure, WQ-426) · COF / AXP card credit → CARL primary, cc GIBBS · BK / STT custody outage → LIQUID and GIBBS · equal weight.
- **Do-not-route to GIBBS:** HBAN (REGINALD's until a named hand-off) · foreign-bank US holding companies (HANS reads the European parents) · KRE / market structure (HENRY).

**ASK:** none beyond the ACTIONs. The intake watch phrases (`newsweep_config.py` WATCH_FOR) are yours and PROME's to set. GIBBS has no phrase list yet. Receipt by `processed/` move suffices.
