# November 9 reopen read and first Monday settle (DOCKET L1089)

**Written:** 2026-11-09 from 12:11 EST (from `date`), live BRENT session on PROME's due-row wake (Will's word 12:07 ET). Runtime Claude Code, Opus 5.5. $0; no trade, card, gate, band, threshold or probability moved unless a section below says so.

**Status of this note:** sections 1 to 5 written before the 14:30 ET settle; section 6 (window and settle) is PENDING until the post-settle capture.

## 1. Reopen against the 11/8 surprise bands

Vendor one-minute bars, `path.py` capture p1 at 12:1x EST (raw in `raw/p1_*.json`), [EST vendor, not settles, about 10 minutes delayed]. Friday reference: BZF27 $98.32 wire settle.

| Segment (ET) | BZF27 low – high | First → last | BZH27 last | CLZ26 first → last |
|---|---|---|---|---|
| Sunday open 18:10 to midnight | 97.08 – 98.42 | 97.58 → 98.34 | 92.94 | 90.44 → 91.31 |
| Asia, 00:00 to 03:00 | 96.14 – 98.33 | 98.33 → 96.87 | 91.67 | 91.29 → 90.12 |
| London morning, 03:00 to 08:00 | 93.63 – 98.32 | 96.86 → **93.88** | 89.53 | 90.13 → 87.40 |
| US, 08:00 to 12:00 | 92.80 – 95.16 | 93.82 → 93.79 | 89.80 | 87.29 → 87.65 |

| 11/8 band (descriptive, never a trigger) | Result |
|---|---|
| Up: above about $103 into Monday London | **No.** Session high $98.42, Sunday evening. |
| Not a surprise: −2% to +4% gap that fades or holds through Asia | The gap itself was −0.7% (97.58) and held through Asia, then failed. |
| **Down: under about $95; M1−M3 toward +$4** | **Yes.** BZF27 broke under $95 in the London morning (93.88 at 08:00 ET, low 92.80 in US hours); BZF27−BZH27 same-minute about +$4.0 at noon. |

**Judgment on my own call:** my 11/8 working model, "a small gap up, not a repricing", was wrong on direction. There was no gap up; the market held Friday's level through Asia and then fell about 4.6% from about 01:00 ET. The fall lines up in time with the Qatar-terms report (OilPrice, two unnamed diplomatic sources; neither government confirms) and Trump's CNN line (strikes "highly unlikely" if a strong deal is signed); timing is not cause, and no primary names a driver. What I under-weighted: Friday had priced a deal and the weekend's events were all access risk without barrels lost, so the weekend could not hold a premium once the deal story moved. The down band says the market read the weekend as noise and the Qatar sequence as advancing; FALCON grades the Qatar terms unconfirmed (FAL-10 not met) and Rubio's "outrageous and ridiculous" is verified at Al Jazeera, so the market is ahead of the verified record.

## 2. MKT-BZ-F-ABOVE-100: what a Monday settle can and cannot do

The REGISTRY header (graded-contract rule ④) says this line **fired 7/23 and has no registered revert; it stays fired whatever either month prints.** My 11/8 report called it "the closest line, $1.68 away, graded only on a Monday settle", which reads as a fresh crossing test. That framing omitted the no-revert letter. Classified: an omission in my own report, not a conflict between rules; the registered letter governs. A Monday settle below $100 un-fires nothing; a settle above $100 fires nothing new. The settle is a distance observation on the pinned contract. Whether a sustained run below $100 should get a revert is a question for Will only if someone proposes one; BRENT proposes none (Will 10/31: fewer rules).

## 3. MKT-CL-F-ABOVE-100: un-fire graded on a settlement basis

This line does revert on its letter (fire history on the row: fired 9/14, un-fired 9/18 and 9/21). Named governing contract CLZ26 (December; CLZ26 expires 11/20, so it governs today).

| Session | CLZ26 settle | Side of $100 | Basis |
|---|---|---|---|
| 10/23 | 103.27 | above | CME FINAL bulletin 205 (read 10/26, before the IP block) |
| 10/26 | 101.76 | above | wire, not an exchange page |
| 10/27 | **99.90** | **below** | wire |
| 10/28 | 102.78 | above | wire, two outlets |
| 10/30 | 104.12 | above | CME PRELIMINARY pair, by the DTN prior-settle control |
| **11/2** | **96.46** | **below** | DTN prior-settle base, Investing.com, vendor row agree (`research/2026-11-04_evening-boot/SETTLEMENT_2026-11-02.md`); one lineage |
| 11/3 | 96.09 | below | DTN settle |
| 11/4 | 88.12 | below | DTN, CNBC |
| 11/5 | 90.52 | below | wire |
| 11/6 | 90.83 | below | CNBC; Bloomberg via Rigzone |

**Grade: UN-FIRED at the 11/2 settle ($96.46) and below on every settle since, through 11/6 ($90.83).** The 10/27 settle ($99.90) was a one-session un-fire, re-crossed 10/28; recorded, it changes nothing today. ⚠️ None of the settles after 10/23 is an exchange read (CME blocks this machine); they are secondary publishers sharing the exchange feed, one lineage. The answer does not depend on any single settle: every settle from 11/2 is at least $3.54 under the line. Today's settle is added in section 6.

## 4. Riyadh Aramco office: severity reconciled

| Source | Says |
|---|---|
| Saudi Energy Ministry | "attempted attack", falling shrapnel, minor damage, no casualties |
| Reuters, AFP witnesses (FALCON 11/8) | windows blown out across several floors; a projectile hit the tower |
| CNN- and BBC-verified video (FALCON 11/9, KB-459) | several floors, windows out; at least one floor badly hit |
| Houthis | "significant damage"; also claim King Khalid airport, Aramco storage sites, Riyadh's financial centre |

**Reconciliation:** the ministry's "minor" understates what verified video shows; the building damage is real and visible across several floors. Neither reading moves oil: an office is not production-class, so FALCON's D 85 rung stays NOT FIRED whatever the damage (FALCON 11/9: "office and storage OUT of class whatever the damage; Abqaiq IN class, claim-only"). The storage and airport claims have no Saudi comment and stay CLAIM-ONLY. STATUS's 11/8 "minor damage (Saudi ministry)" is now carried with the verified-video qualifier. COR-20261108-02 is a different correction (the NBC oil-and-gas target line) and is unaffected; it stays APPLIED.

## 5. JPMorgan and Goldman oversupply call against THESIS Phase 2

Claim, relayed: JPMorgan estimates a global surplus of 1.1 mb/d in September widening to 1.4 mb/d in October; Goldman says the market is moving back toward oversupply as high prices cut demand (Reuters via Lufkin Daily News, 11/9; OilPrice 11/6) [EST, relay, bank estimates, not measurements]. JPMorgan's figure was already logged on combo:paper-physical-gap on 11/5 from a different relay.

| THESIS item | How the call reads against it |
|---|---|
| Phase 2, Path B (demand weakening) | Consistent with it globally, and with the IEA's 10/14 finding of global demand contraction. It is a model estimate of a balance, not the registered US test. |
| BRT-31 (registered US Path-B test) | Unchanged: four non-qualifying weeks; next WPSR Thursday 11/12. A bank surplus estimate cannot grade it. |
| Physical record | Cuts against an actual surplus showing up yet: Dated Brent $107.03 on 11/3 against BZF27 $103.60 that day; US distillate 99.259M, lowest since 2003; M1−M3 still backwardated (about +$4.0 at noon today). A 1.4 mb/d surplus would build stocks and flatten the prompt curve; the prompt curve is flattening, the stock prints have not shown it. |
| Saudi pricing | Aramco's December Asia OSP cut (−$2) fits the weak-Asian-physical side of the call. |

**Read:** this strengthens the paper side of the paper-physical gap, not Phase 2 on the letter. No phase transition, version change or probability move. The resolvers are physical: EIA's November STEO balance (Tuesday 11/10), the IEA OMR, and Thursday's WPSR. Logged on combo:paper-physical-gap.

## 6. Window and settle, Monday 11/9

PENDING: capture after 14:45 ET.
