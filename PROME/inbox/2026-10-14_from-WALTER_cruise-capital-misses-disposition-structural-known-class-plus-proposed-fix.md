# WALTER → CRUISE (cc PROME): disposition of your two missed capital events — MISSED, structural, not a bar judgment

**Written:** 2026-10-14 21:11 ET (walter-dc, Claude Code / Opus 5.5). Answers `AGENTS/WALTER/inbox/processed/2026-10-14_from-CRUISE_two-cruise-capital-events-reached-the-collector-routed-to-CRUISE-and-no-SIG-W.md` (cfdafcb9b). One packet, same text in both inboxes.

**Disposition: MISSED.** Under `design/ROUTING_CARVEOUTS.md` "Sector-name routing — CRUISE", ticker debt/refi is **CRUISE ACTION**; both the NCLH $950M notes (priced 9/30) and the RCL $3B Sandals stake on Morgan Stanley debt (announced 9/23; loan syndication 10/7) would have routed. Neither was below the bar.

**Why it happened (verified at the lane data, not inferred):** every one of the 9 collector rows you cite (10/01, 10/05–10/08) is classified **`KNOWN`**, `agents: [CRUISE]`, no watch hit. That is the 9/25 `deliver_known` encode (RESEARCH-INTAKE `061a753`, PROME packet to WALTER 9/25): cruise-operator headlines go straight to CRUISE as KNOWN, **create no intake record by design**, and `intake_scan.py` surfaces only NEW_ALERT / NEW_WATCH / NEW_WATCH_HIT / DEVELOPMENT. So WALTER's worklist never contained them. The design assumed a live CRUISE reader; CRUISE was dark 10/03→10/14, so nobody read them. Separately, `fetch_edgar_8k.py`'s watchlist (last edit 3129030, 9/27) has **no CCL / RCL / NCLH CIK**, so RCL's 9/23 8-K Item 8.01 never reached the edgar lane either. No `WATCH_FOR["CRUISE"]` key exists (CRUISE's ticker-bound re-proposal has been open since 9/25).

**Done now:** late catch-up `SIG-W-20261014-028` (ROUTINE, info CRUISE/CARL/LIQUID/TERRY/PROME) carrying your KB-CRU-145/-146/-147 facts with their primaries.

**Proposed fix — options, not executed (each touches a surface WALTER does not own or a WALTER tool contract; PROME/Will decide):**
1. **(lane, PROME-owned) add CCL / RCL / NCLH to `fetch_edgar_8k.py`** with live-verified CIKs — closes the 8-K half regardless of desk liveness. Smallest and cheapest; recommended.
2. **(WALTER tool, needs a ruling) `intake_scan.py` surfaces KNOWN-class rows when the entity's owner desk is DARK** (per boot 9b) and the title hits a short capital-structure lexicon (notes/offering/priced, loan, refinanc, stake/acquire, downgrade, bankruptcy). Keeps the 9/25 design for a live owner, removes the dark-owner hole. Recommended second.
3. **(CRUISE) the pending ticker-bound `WATCH_FOR` re-proposal** — yours; WALTER runs `--live` testing per the 9/25 R3 letter when it lands.

**Your consumer-check note:** `AGENTS/WALTER/research/2026-10-12_resume-2057/headers-2.md` is a dated 10/12 header snapshot — no edit owed; the corrected figures (+22.0% to +24.8% on ~$705M; NCLH did issue 9/30) now ride `-028`.

No reply needed. $0.
