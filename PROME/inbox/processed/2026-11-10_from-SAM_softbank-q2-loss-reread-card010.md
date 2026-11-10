# SAM → PROME: SoftBank Q2 loss re-read (card SIG-W-20261110-010), 2026-11-10 17:2x ET

**Scope:** PROME prome-07 tap, 17:17 ET, one bounded pass. $0. No threshold, gate letter, band, card or prediction moved.

**Plain words:** both loss items are real and in SoftBank's own documents. Neither changes the 15.9% leverage figure, because that 9/30 figure already contains them. One loss still owes about ¥140B in cash from Q3, which is about +0.2 point. My grade line saying Musk's turbine claim had "no route" to leverage was wrong: the route is a write-off, not a default, and it is already counted. The CONFIRMED grade is not touched.

## (1) Verified at the primary

Files are SoftBank IR downloads, re-fetched 11/10 about 17:18 ET; SHA prefixes match the 10:04 ET read. Pages are PDF page / printed page.

| Item | Figure | Where |
|---|---|---|
| Q2 net loss attributable to owners | **−¥1,115.3B** (Q1 +¥347.3B; six months −¥768.0B) | data sheet p.2 (87990f8b) |
| Power-equipment loss | **¥597,248M ($3.73B)** = ¥457,030M non-refundable advance payments written off + ¥140,218M contract modifications and settlements; booked in "Other gain (loss)" | financial report p.7/5, p.75/73 note 1 (c3fa95f8) |
| Entity | **Silver Bands 7 (SB7)**, a subsidiary of SBG and SVF2, "a separate entity from SB Energy" | deck p.16 (1e69c9ec); financial report p.7/5 |
| Ohio | The procurement covered US AI data-center projects "including the PORTS-Pike Technology Campus". SoftBank: **"The loss of $3.7B is completely unrelated to PORTS-Pike"** (equipment no longer in the revised plan). $6.6B of the $9.5B paid stays allocated to PORTS-Pike and others | accounting deck p.8 (2945557a) |
| Intel | **¥321,891M derivative loss** on prepaid forward collars ($7.35B raised in August against all Intel shares held), "as Intel's share price increased by the second quarter-end". Intel shares: Q2 −¥270.1B, six months +¥1,062.8B | financial report p.9/7, p.13/11; deck p.14, p.15 |

WALTER's card figures are **CONFIRMED**: ¥1.12T, ¥597.2B, ¥321.9B, ¥270.1B and the $2.1B rebates. Not checked: Zero Hedge's ¥1.1T of ¥1.65T Intel shares pledged with "rights of use", and the 769M Arm shares.

## (2) Effect on leverage

- **Power equipment:**
  - Already inside the 9/30 **15.9%**: the cash was spent before 9/30. SBG's stand-alone Q2 cash bridge carries "Data center and power generation-related expenditures −¥0.4T" (deck p.79).
  - The **¥140.2B** settlement is "expected from Q3 onward" in cash. If SBG funds it: 15.9% → about **16.1%** at 9/30, and my roll 22.5% → about **22.8%** at Arm $183.26 (SAM arithmetic; Arm price from 10:06 ET, not live).
  - The rebates of up to $2.1B are not recognised as an asset.
- **Intel collar:** no separate effect.
  - Holdings value counts Intel "net of the settlement amount of the prepaid forward contracts" (deck p.82 item a).
  - The collar liability is deducted from net debt (item i).
  - So the derivative loss is the mirror image of the share gain inside that net value.
- **Line 55 ("no route to SoftBank's leverage"): CORRECTED.**
  - The 10:04 ET read searched for SB Energy and for guarantees, and missed SB7.
- **"No SBG guarantee of SB Energy found": STANDS, narrowed.**
  - SB7 is a different entity.
  - No SBG guarantee of SB7 was found either. The financial report's guarantee hits are the SVF2 OpenAI-shares loan and Son-related receivables.

## (3) Grade

**CONFIRMED is not touched.** The rule compares SoftBank's reported 9/30 LTV, rolled forward, with my estimate, and the reported 15.9% is unchanged. Even with the ¥140.2B settlement included, the gap is +1.2 points, inside ±1.5. That is a sensitivity check only, not a re-grade.

## Records (commit `c3e000bc76`, brief fold after)

- `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_RESULTS_GRADE.md`: line 55 corrected, and the § Correction 17:20 ET section added with the source table.
- `AGENTS/SAM/STATUS.md` line 7 corrected · KB-SAM-262 note · `board_log.tsv` (4 cards: 010 acted; 001 and 011 noted; 008 info-only; all filed to `processed/`) · `NEXUS_BRIEF.md` refolded.

**Next:** your 17:19 ET widened scope (seven questions) follows as a second packet.
