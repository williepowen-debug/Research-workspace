# Bounded backlog review, 2026-11-11 (Will 13:33 ET)

Scope as directed: the lane searches `position-banks` and `bank-vendor-incidents-msp` / `-core`, batches 2026-10-12 to 2026-11-10. No other family reviewed; no permanent review added. Item list with scanner classes: `items.tsv` (147 unique titles).

## Measurement, corrected
- My earlier table counted only `level` alert/watch. The scanner also handles `NEW_WATCH_HIT` and `DEVELOPMENT` per item (intake_scan.py, since 9/25), and `NEW_ALERT` / `NEW_WATCH` as a count with a pointer to the day's file. CATO's correction holds: **9 bank and 36 vendor titles were eligible.** Eligibility is not review.
- My displayed table sums to **482** titles before deduplication, not 450 (and not 580); the insurer figure was approximate.
- **Limit found in the scanner itself:** per-item hits are read from the **latest batch only**. A batch is shown only if WALTER runs while it is the newest.

## Eligibility vs display (seen-file history, 31 revisions since 10/10)
40 of 45 eligible titles were in WALTER's scan output when it marked them. Display is not review or consumption. The 5 never displayed:

| Title | Disposition |
|---|---|
| WAL Q3 results release, 10/20 | **Previously covered:** WAL desk read the Q3 release and call itself (KB-WAL-248 to -250, research/2026-10-19_Q3_FULL_READ.md) |
| Volleyball at Bank OZK Arena | noise |
| ConnectWise MSP impact follow-on, 11/2 | **Previously covered:** ConnectWise on 10 BOARD cards, 11 CYPHER files |
| TruStage human-interest repost ×2, 11/7 | **Previously covered:** TruStage on 4 BOARD cards, 9 CYPHER files; same story displayed 11/11 |

Every displayed vendor event (ConnectWise, Jack Henry, Finastra, Sharetec, Abrigo/Sageworks, TruStage, N-able July flaw, Fiserv) is on the BOARD and in CYPHER's records. Several "new" headlines were old events with fresh feed dates: Finastra ransomware is March 2020; Finastra's Krebs breach is November 2024; Sharetec is September 2026; Jack Henry's breach is August 2026.

## Not eligible (102 titles)
- **Bank family (40): all noise.** "WAL" matches Walmart, Walsall, Wal-Mart de México and Oromo-language "wal"; one Black Hills legal notice; a construction-lender office item.
- **Vendor family (62):** mostly old Sharetec, Finastra and Fiserv items, ConnectWise follow-ons, ClassAction.org solicitations and roundups. Three new items:

| Item | Classification | Action |
|---|---|---|
| **N-able took N-central offline worldwide 11/9 after 33 alleged zero-days ("Able2Shell"); no exploitation confirmed; hotfix pending** (11 headlines 11/9–11/10) | **Demonstrably missed by WALTER's intake:** collected, not eligible (no watch phrase matched "zero-days" or "offline"), no BOARD card or CYPHER record. Whether CYPHER saw it elsewhere: **Unresolved** (no CYPHER session since 11/8). | Routed SIG-W-20261111-022, CYPHER action, PRIORITY |
| Suncoast Credit Union breach claim (ClassAction.org, 11/3) | Not in CYPHER's claims card 20261109-003 or records; low-quality source | Claims line on card 022 |
| Jack Henry "incident not financially material" (11/3) | Follow-on to CYPHER CYB-INC-048 | Line on card 022 |

## Why the miss happened
CYPHER's watch phrases key on incident words (ransomware, breach, cyberattack, outage). The N-able story used "zero-days" and "offline". The phrase list matched the class, not every wording of it. Per-item display also depends on WALTER running while the batch is newest.

## Research significance
N-able is a candidate member of CYPHER's existing supplier-route theme (KB-CYP-098). It is a vendor-wide shutdown of a monitoring tool used by the managed-service providers that most community banks outsource to. No bank or credit-union impact is reported, and N-able reports no exploitation. It does not change an assessment on its own. It is a timely question for CYPHER: is there a bank consequence, and does it belong on an escalation-watch row?

## Recommendation
**No new recurring review.** In 30 days, the two families produced one real miss among 147 titles. The miss is a phrase-coverage gap, not an unread pile. Proportionate fix, for CYPHER to decide at its owner session: consider adding watch phrases such as "N-able zero-day", "N-central offline", or a vendor-name-plus-"offline"/"zero-day" pair to its WATCH_FOR list, harness-tested first (MEMORY #58). WALTER does not edit CYPHER's phrases. Bank family: the `position-banks` query is mostly noise ("WAL"); its owner may want it narrowed. No change proposed by WALTER.

## Other backlog items
- CATO SIG-W-20261019-012: description corrected in STATUS and LAST_COMPLETION (CATO's 10/19 run 566c749dc incorporated the substance; only the exact receipt is unrecorded). No receipt invented, no new assignment.
- Calendars: Michigan sentiment (HENRY) and OPEC MOMR (BRENT) still had no rows; flagged by packet and message (a34c796f9d).
- Unread sources: CF call read by FERT (KB-FERT-136); BoE 11/5 decision held by HANS (KB-HANS-164); STWD, ACRE and RC filings read by CREED (KB-CREED-113, -117, VX-CREED-10.01). WALTER rereads none.
- 11/4 ISHM and LIQUID packets: retrospective consume declarations added from WALTER's own moving commits (f3152bf6ac, baa25ef70e); read times stay unrecorded.
- DOORBELL_LOG rows for November 2–4: no evidence found to reconstruct them; left UNKNOWN rather than invented.
